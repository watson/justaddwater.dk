#!/usr/bin/env python3
"""Validate content coverage, local links and static-only archive behavior."""
import argparse
from collections import Counter
import html
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, unquote_plus, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from archive import ROOT, HOSTS, CSS_URL, embedded_css, is_video_embed, parse_document
from recovery import recovery_data, SHORTCODE, UNDO_PATH, TABLE_DEMO, BUTTON_DEMO
from feeds import feed_specs, comment_items, ATOM, url_path


def video_embed_markup(soup):
    # Compare the original markup directly, including object params, nested
    # embeds, dimensions and URLs. Do not sanitize the expected players.
    return Counter(str(tag) for tag in soup.find_all(['iframe', 'object', 'embed'])
                   if is_video_embed(tag))


def expected_article_content(soup):
    # Deliberately independent of clean_html: applying the converter's cleanup
    # to both expected and actual content would hide its accidental deletions.
    for tag in soup.find_all(['script', 'style', 'iframe', 'object', 'embed', 'applet']):
        tag.decompose()
    return soup


def archived_form_errors(soup):
    errors = []
    for group in soup.select('.archive-form'):
        if group.name != 'div' or group.get('aria-disabled') != 'true' or group.find('form'):
            errors.append('archived form is not a disabled display')
        if any(group.has_attr(attr) for attr in ('action', 'method', 'enctype', 'target')):
            errors.append('archived form retains submission attributes')
        for control in group.find_all(['input', 'textarea', 'select', 'button']):
            if not control.has_attr('disabled'):
                errors.append('archived form has an enabled control')
            if any(control.has_attr(attr) for attr in ('form', 'formaction', 'formmethod', 'formenctype', 'formtarget', 'autofocus', 'tabindex')):
                errors.append('archived form control retains submission or focus attributes')
        notices = [soup.find(id=id) for id in group.get('aria-describedby', '').split()]
        if not any(note is not None and 'archive-form-notice' in note.get('class', [])
                   and 'This form no longer accepts submissions.' in note.get_text() for note in notices):
            errors.append('archived form is missing its notice')
    return errors


def article_text_preserved(markup, actual):
    # Independently check approved snippet text and every remaining prose node.
    # Do not run the converter's restore_code/clean_html on the expectation.
    replacements = {block['captured']: block['code'] for block in recovery_data()['code_blocks']}
    markup = SHORTCODE.sub(lambda match: '<pre>' + html.escape(replacements[match[0]], quote=False) + '</pre>'
                           if match[0] in replacements else match[0], markup)
    for row in recovery_data()['tag_lists']:
        # get_text(' ', strip=True) separates the link labels and comma nodes.
        markup = markup.replace(row['captured'], 'Technorati Tags: ' + ' , '.join(row['tags']))
    def expected_text(text):
        return ' '.join(text.split())

    original = BeautifulSoup(markup, 'html.parser')
    expected = expected_text(expected_article_content(original).get_text(' ', strip=True))
    if expected in actual:
        return True
    # An unclosed table in an old article can make the browser move surrounding
    # text before its cells, even inserting the page footer between them. Check
    # every complete text node in browser order, allowing template text between
    # nodes, instead of treating that original rendering as lost content.
    browser_content = expected_article_content(parse_document(markup, recover=False))
    position = 0
    for node in browser_content.stripped_strings:
        text = expected_text(node)
        position = actual.find(text, position)
        if position < 0:
            return False
        position += len(text)
    return True


def verify(site, base):
    site = site.resolve()
    base = '/' + base.strip('/') if base.strip('/') else ''
    errors, local_links, comment_ids, archived_forms = [], 0, set(), 0
    external_images = Counter()
    data = json.loads((ROOT / 'data/content.json').read_text())
    expected_videos = {row['id']: video_embed_markup(BeautifulSoup(row['content']['rendered'], 'html.parser'))
                       for row in data['posts'] + data['pages']}
    original_players = {markup for players in expected_videos.values() for markup in players}
    recovery = recovery_data()
    snapshots = json.loads((ROOT / 'data/comment-feeds.json').read_text())
    post_guids = json.loads((ROOT / 'data/post-feed-ids.json').read_text())
    feeds = feed_specs(data, snapshots['feeds'])
    expected_code = {block['id']: block['code'] for block in recovery['code_blocks']}
    expected_code.update({f'gist-{gist["post_id"]}-{index + 1}': file['code']
                          for gist in recovery['gists'].values() for index, file in enumerate(gist['files'])})
    seen_code = set()
    page_comment_ids = {}

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
            result /= 'index.html' if (result / 'index.html').is_file() else 'index.xml'
        local_links += 1
        if not result.is_file():
            errors.append(f'{document.relative_to(site)}: missing {url}')
        return result

    def check_css(css, document):
        for match in CSS_URL.finditer(css):
            if urlsplit(match[2]).hostname:
                errors.append(f'{document.relative_to(site)}: remote CSS dependency: {match[2]}')
            target(match[2], document)

    pages = list(site.rglob('*.html'))
    for file in pages:
        soup = BeautifulSoup(file.read_bytes(), 'html.parser')
        page_comment_ids[file] = set()
        relative = '/' + file.relative_to(site).as_posix()
        for tag in soup.find_all(True):
            if tag.name == 'script':
                allowed = {base + '/archive-assets/archive.js'}
                if relative == TABLE_DEMO:
                    allowed.add(base + '/archive-assets/demos.js')
                elif relative == UNDO_PATH:
                    allowed.add('../demos.js')
                if tag.get('src') not in allowed or tag.get_text().strip():
                    errors.append(f'{file}: unexpected executable script')
            local_demo = (tag.name == 'iframe' and tag.get('src') == base + UNDO_PATH
                          and tag.get('sandbox') == ['allow-scripts'])
            if tag.name in ('iframe', 'object', 'embed', 'applet') and str(tag) not in original_players and not local_demo:
                errors.append(f'{file}: embed differs from original video players')
            if any(attr.lower().startswith('on') for attr in tag.attrs):
                errors.append(f'{file}: inline event handler')
            if tag.get('id') and re.fullmatch(r'comment-\d+', tag['id']):
                comment_ids.add(int(tag['id'].split('-')[-1]))
                page_comment_ids[file].add(tag['id'])
            for attr in ('href', 'src', 'poster', 'data', 'action'):
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
        for css in embedded_css(soup):
            check_css(css, file)
        for form in soup.find_all('form'):
            if form.get('method', 'get').lower() != 'get' or urlsplit(form.get('action', '')).path != base + '/search/':
                errors.append(f'{file}: non-static form')
        archived_forms += len(soup.select('.archive-form'))
        errors.extend(f'{file}: {error}' for error in archived_form_errors(soup))
        for block in soup.select('[data-recovery-code]'):
            key = block['data-recovery-code']
            seen_code.add(key)
            if block.get_text() != expected_code.get(key):
                errors.append(f'{file}: recovered example differs: {key}')
        for block in soup.select('[data-recovery-tags]'):
            row = next((r for r in recovery['tag_lists'] if str(r['post_id']) == block['data-recovery-tags']), None)
            links = block.find_all('a')
            if (row is None or block.name != 'small'
                    or block.get_text() != 'Technorati Tags: ' + ', '.join(row['tags'])
                    or [a.get_text() for a in links] != row['tags']
                    or any(a.get('rel') != ['tag'] or not a.get('href', '').startswith('http://technorati.com/tag/')
                           or unquote_plus(a['href'].removeprefix('http://technorati.com/tag/')) != a.get_text() for a in links)):
                errors.append(f'{file}: repaired tag list differs from SimpleTags output')

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
        actual = ' '.join(soup.get_text(' ', strip=True).split())
        if not article_text_preserved(row['content']['rendered'], actual):
            errors.append(f'Published article text differs from API export: {row["link"]}')
        if video_embed_markup(soup) != expected_videos[row['id']]:
            errors.append(f'Published video players differ from API export: {row["link"]}')
        if url_path(row['link']) + 'feed/' in snapshots['feeds']:
            expected_feed = base + url_path(row['link']) + 'feed/'
            for link in soup.select('.postmetadata.alt a'):
                if link.get_text(strip=True) == 'RSS 2.0' and link.get('href') != expected_feed:
                    errors.append(f'Article RSS link does not preserve its comment feed path: {row["link"]}')
        if any(r['post_id'] == row['id'] for r in recovery['tag_lists']):
            if len(soup.select(f'[data-recovery-tags="{row["id"]}"]')) != 1:
                errors.append(f'Published article is missing its repaired tag list: {row["link"]}')
        for key, code in expected_code.items():
            if key.startswith((f'post-{row["id"]}-', f'gist-{row["id"]}-')):
                block = soup.find(attrs={'data-recovery-code': key})
                if block is None or block.get_text() != code:
                    errors.append(f'Published article is missing recovered example {key}: {row["link"]}')
        content_checks += 1
    for asset in recovery['assets']:
        file = site / asset['path'].lstrip('/')
        if not file.exists() or hashlib.sha256(file.read_bytes()).hexdigest() != asset['sha256']:
            errors.append(f'Recovered asset missing or modified: {asset["path"]}')
    for alias, canonical in recovery['aliases'].items():
        file, original = site / alias.lstrip('/'), site / canonical.lstrip('/')
        if not file.exists() or file.read_bytes() != original.read_bytes():
            errors.append(f'Repaired asset alias missing or modified: {alias}')
    for path, selector, count in [(UNDO_PATH, '#done', 1), (BUTTON_DEMO, 'input, button', 3)]:
        soup = BeautifulSoup((site / path.lstrip('/')).read_bytes(), 'html.parser')
        controls = soup.select(selector)
        if (len(controls) != count or any(c.has_attr('disabled') for c in controls)
                or soup.select('form, [aria-disabled], .archive-form-notice')
                or any(c.has_attr(attr) for c in controls for attr in ('form', 'formaction'))):
            errors.append(f'Local demo controls are disabled or can submit: {path}')
    missing_comments = {row['id'] for row in data['comments']} - comment_ids
    if missing_comments:
        errors.append(f'{len(missing_comments)} public comments missing from HTML: {sorted(missing_comments)[:20]}')
    for comment in recovery['comments']:
        file = site / comment['path'].lstrip('/') / 'index.html'
        soup = BeautifulSoup(file.read_bytes(), 'html.parser')
        matches = soup.find_all(id=f'comment-{comment["id"]}')
        if len(matches) != 1:
            errors.append(f'Recovered comment missing or duplicated: {comment["id"]}')
            continue
        item = matches[0]
        if (item.cite is None or item.cite.get_text() != comment['author']
                or item.p is None or item.p.get_text() != comment['content']
                or item.time is None or item.time.get('datetime') != comment['date'].replace(' ', 'T')
                or comment['type'] not in item.get('class', [])):
            errors.append(f'Recovered comment differs from reviewed content: {comment["id"]}')

    for file in site.rglob('*.css'):
        check_css(file.read_text(), file)
    for path, spec in feeds.items():
        file = site / unquote(path).lstrip('/') / 'index.xml'
        try:
            root = ET.parse(file).getroot()
            atom = spec.get('format') == 'atom'
            channel = root if atom else root.find('channel')
            prefix = f'{{{ATOM}}}' if atom else ''
            if channel is None or channel.findtext(prefix + 'title') != spec['title']:
                errors.append(f'Wrong RSS channel: {path}')
                continue
            items = channel.findall(prefix + 'entry' if atom else 'item')
            if spec['kind'] == 'comments':
                expected = comment_items(spec, data, snapshots)
                expected_guids = [row['guid'] for row in expected]
                if [i.findtext('pubDate') for i in items] != [row['date'] for row in expected]:
                    errors.append(f'RSS comment timestamps differ: {path}')
            else:
                expected_guids = [post_guids[str(row['id'])] for row in spec['posts']]
            if [i.findtext(prefix + 'id' if atom else 'guid') for i in items] != expected_guids:
                errors.append(f'RSS contains the wrong entries: {path}')
            self_link = channel.find(f'{{{ATOM}}}link[@rel="self"]')
            if self_link is None or urlsplit(self_link.get('href', '')).path != base + path:
                errors.append(f'RSS self link does not preserve its path: {path}')
            if file.with_name('index.html').exists():
                errors.append(f'HTML masks the RSS directory URL: {path}')
            for item in items:
                link = item.find(f'{{{ATOM}}}link').get('href', '') if atom else item.findtext('link', '')
                expected_host = urlsplit(self_link.get('href', '')).netloc if self_link is not None else ''
                if urlsplit(link).netloc != expected_host or not urlsplit(link).path.startswith(base + '/'):
                    errors.append(f'RSS entry links outside the deployed archive: {path}')
                document = target(urlsplit(link).path, file)
                if spec['kind'] == 'comments' and urlsplit(link).fragment not in page_comment_ids.get(document, set()):
                    errors.append(f'RSS comment link does not locate its preserved comment: {link}')
        except (OSError, ET.ParseError) as error:
            errors.append(f'{file}: invalid RSS: {error}')
    for file in [site / 'sitemap.xml']:
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
               'articles_with_video_players': sum(bool(players) for players in expected_videos.values()),
               'recovered_code_examples': len(seen_code),
               'disabled_archived_forms': archived_forms,
               'public_comments': len(comment_ids), 'local_links_checked': local_links,
               'recovered_comments': len(recovery['comments']),
               'rss_feeds': len(feeds),
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
