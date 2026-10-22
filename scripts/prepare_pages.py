#!/usr/bin/env python3
"""Copy site/ into a deploy directory, optionally under a project URL prefix."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil

from feeds import deploy_feed

ROOT = Path(__file__).resolve().parents[1]


def prefix_css(text, base):
    return re.sub(r'(url\([\"\']?)/(?!/)', lambda m: m[1] + base + '/', text)


class PrefixHTML(HTMLParser):
    """Rewrite actual tag attributes while leaving article/code text intact."""
    def __init__(self, base):
        super().__init__(convert_charrefs=False)
        self.base, self.parts, self.in_style = base, [], False

    def handle_starttag(self, tag, attrs):
        text = self.get_starttag_text()
        text = re.sub(r'((?:href|src|action|poster)=[\"\'])/(?!/)', lambda m: m[1] + self.base + '/', text)
        text = prefix_css(text, self.base)
        text = re.sub(r'(srcset=[\"\'])(.*?)([\"\'])',
                      lambda m: m[1] + re.sub(r'(^|,\s*)/(?!/)', lambda n: n[1] + self.base + '/', m[2]) + m[3], text)
        self.parts.append(text)
        if tag == 'style':
            self.in_style = True

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        self.parts.append(f'</{tag}>')
        if tag == 'style':
            self.in_style = False

    def handle_data(self, data):
        self.parts.append(prefix_css(data, self.base) if self.in_style else data)

    def handle_entityref(self, name):
        self.parts.append(f'&{name};')

    def handle_charref(self, name):
        self.parts.append(f'&#{name};')

    def handle_comment(self, data):
        self.parts.append(f'<!--{data}-->')

    def handle_decl(self, decl):
        self.parts.append(f'<!{decl}>')

    def handle_pi(self, data):
        self.parts.append(f'<?{data}>')


def prepare(destination, base_path, site_url=None):
    base = '/' + base_path.strip('/') if base_path.strip('/') else ''
    if not re.fullmatch(r'(?:/[A-Za-z0-9._-]+)*', base):
        raise ValueError('Invalid deployment base path')
    site_url = site_url or ('https://watson.github.io' + base if base else 'https://justaddwater.dk')
    source = ROOT / 'site'
    destination = destination.resolve()
    if destination == ROOT or destination == source or source.is_relative_to(destination):
        raise ValueError('Output must be separate from the source tree')
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)
    for path in destination.rglob('*'):
        if path.name == 'index.xml':
            path.write_text(deploy_feed(path.read_text(), site_url))
        elif base:
            if path.suffix.lower() not in ('.html', '.css'):
                continue
            text = path.read_text()
            if path.suffix.lower() == '.html':
                parser = PrefixHTML(base)
                parser.feed(text)
                parser.close()
                text = ''.join(parser.parts)
            else:
                text = prefix_css(text, base)
            path.write_text(text)
    print(f'Prepared {destination} with base path {base or "/"}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-path', default='')
    parser.add_argument('--site-url', help='Absolute deployed site URL used inside RSS feeds')
    parser.add_argument('--output', type=Path, default=ROOT / '_site')
    args = parser.parse_args()
    prepare(args.output, args.base_path, args.site_url)
