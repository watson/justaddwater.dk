#!/usr/bin/env python3
"""Validate content coverage, local links and static-only archive behavior."""
import argparse
from collections import Counter
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from archive import ROOT, HOSTS, CSS_URL, clean_html


def verify(site, base):
    site = site.resolve()
    base = '/' + base.strip('/') if base.strip('/') else ''
    errors, local_links, comment_ids = [], 0, set()
    external_images = Counter()
    data = json.loads((ROOT / 'data/content.json').read_text())

    def target(url, document):
        nonlocal local_links
        parts = urlsplit(html.unescape(url))
        if parts.scheme or parts.netloc or not parts.path:
            return None
        path = unquote(parts.path)
        if path.startswith('/'):
            if base:
                if not path.startswith(base + '/'):
                    errors.append(f'{document}: link escaped deployment prefix: {url}')
                    return None
                path = path[len(base):]
            result = site / path.lstrip('/')
        else:
            result = document.parent / path
        result = result.resolve()
        if not result.is_relative_to(site):
            errors.append(f'{document}: path escaped site: {url}')
            return None
        if result.is_dir():
            result /= 'index.html'
        local_links += 1
        if not result.is_file():
            errors.append(f'{document.relative_to(site)}: missing {url}')
        return result

    pages = list(site.rglob('*.html'))
    for file in pages:
        soup = BeautifulSoup(file.read_bytes(), 'html.parser')
        for tag in soup.find_all(True):
            if tag.name == 'script' and tag.get('src') != base + '/archive-assets/archive.js':
                errors.append(f'{file}: unexpected executable script')
            if tag.name in ('iframe', 'object', 'embed', 'applet'):
                errors.append(f'{file}: active legacy embed')
            if any(attr.lower().startswith('on') for attr in tag.attrs):
                errors.append(f'{file}: inline event handler')
            if tag.get('id') and re.fullmatch(r'comment-\d+', tag['id']):
                comment_ids.add(int(tag['id'].split('-')[-1]))
            for attr in ('href', 'src', 'poster', 'action'):
                url = tag.get(attr)
                if not url:
                    continue
                if url.lower().startswith(('javascript:', 'vbscript:')):
                    errors.append(f'{file}: executable URL')
                if urlsplit(url).hostname in HOSTS and tag.get('rel') not in (['canonical'], ['shortlink']):
                    errors.append(f'{file.relative_to(site)}: depends on old host: {url}')
                target(url, file)
            if tag.name == 'img' and urlsplit(tag.get('src', '')).hostname:
                external_images[urlsplit(tag['src']).hostname] += 1
            if tag.get('srcset'):
                for item in tag['srcset'].split(','):
                    if item.strip():
                        target(item.strip().split()[0], file)
            if tag.get('style'):
                for match in CSS_URL.finditer(tag['style']):
                    target(match[2], file)
        for form in soup.find_all('form'):
            if form.get('method', 'get').lower() != 'get' or urlsplit(form.get('action', '')).path != base + '/search/':
                errors.append(f'{file}: non-static form')

    content_checks = 0
    for row in data['posts'] + data['pages']:
        path = unquote(urlsplit(row['link']).path)
        file = site / path.lstrip('/') / 'index.html'
        if not file.exists():
            errors.append(f'Missing published article: {row["link"]}')
            continue
        soup = BeautifulSoup(file.read_bytes(), 'html.parser')
        title = BeautifulSoup(row['title']['rendered'], 'html.parser').get_text(' ', strip=True)
        if ' '.join(title.split()) not in ' '.join(soup.get_text(' ', strip=True).split()):
            errors.append(f'Published title missing: {row["link"]}')
        expected = ' '.join(clean_html(BeautifulSoup(row['content']['rendered'], 'html.parser')).get_text(' ', strip=True).split())
        actual = ' '.join(soup.get_text(' ', strip=True).split())
        if expected not in actual:
            errors.append(f'Published article text differs from API export: {row["link"]}')
        content_checks += 1
    missing_comments = {row['id'] for row in data['comments']} - comment_ids
    if missing_comments:
        errors.append(f'{len(missing_comments)} public comments missing from HTML: {sorted(missing_comments)[:20]}')

    for file in site.rglob('*.css'):
        for match in CSS_URL.finditer(file.read_text()):
            target(match[2], file)
    for file in [site / 'sitemap.xml', site / 'feed/index.xml', site / 'comments/feed/index.xml']:
        try:
            ET.parse(file)
        except (OSError, ET.ParseError) as error:
            errors.append(f'{file}: invalid XML: {error}')
    for file in site.rglob('*'):
        if file.is_symlink():
            errors.append(f'Symlink is not supported by GitHub Pages: {file}')
        if file.is_file() and file.stat().st_size > 95 * 1024 * 1024:
            errors.append(f'File too large for regular Git: {file}')
    if external_images:
        errors.append(f'Remote image dependencies remain: {dict(external_images)}')
    summary = {'html_pages': len(pages), 'published_posts_and_pages': content_checks,
               'public_comments': len(comment_ids), 'local_links_checked': local_links,
               'errors': len(errors), 'deployment_base': base or '/'}
    print(json.dumps(summary, indent=2))
    for error in errors[:80]:
        print(error, file=sys.stderr)
    if len(errors) > 80:
        print(f'… {len(errors) - 80} further errors', file=sys.stderr)
    return bool(errors)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=ROOT / 'site')
    parser.add_argument('--base-path', default='')
    args = parser.parse_args()
    sys.exit(verify(args.site, args.base_path))
