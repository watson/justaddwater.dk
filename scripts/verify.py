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
from archive import ROOT, HOSTS, CSS_URL, embedded_css, is_video_embed, parse_document


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
    for form in soup.find_all('form'):
        # Genuine submission UI is intentionally absent from the archive.
        # A bare form tag in an example must not exclude the prose after it.
        if form.find(['input', 'textarea', 'select', 'button']):
            form.decompose()
    return soup


def article_text_preserved(markup, actual):
    expected = ' '.join(expected_article_content(BeautifulSoup(markup, 'html.parser')).get_text(' ', strip=True).split())
    if expected in actual:
        return True
    # An unclosed table in an old article can make the browser move surrounding
    # text before its cells, even inserting the page footer between them. Check
    # every complete text node in browser order, allowing template text between
    # nodes, instead of treating that original rendering as lost content.
    browser_content = expected_article_content(parse_document(markup))
    position = 0
    for node in browser_content.stripped_strings:
        text = ' '.join(node.split())
        position = actual.find(text, position)
        if position < 0:
            return False
        position += len(text)
    return True


def verify(site, base):
    site = site.resolve()
    base = '/' + base.strip('/') if base.strip('/') else ''
    errors, local_links, comment_ids = [], 0, set()
    external_images = Counter()
    data = json.loads((ROOT / 'data/content.json').read_text())
    expected_videos = {row['id']: video_embed_markup(BeautifulSoup(row['content']['rendered'], 'html.parser'))
                       for row in data['posts'] + data['pages']}
    original_players = {markup for players in expected_videos.values() for markup in players}

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

    def check_css(css, document):
        for match in CSS_URL.finditer(css):
            if urlsplit(match[2]).hostname:
                errors.append(f'{document.relative_to(site)}: remote CSS dependency: {match[2]}')
            target(match[2], document)

    pages = list(site.rglob('*.html'))
    for file in pages:
        soup = BeautifulSoup(file.read_bytes(), 'html.parser')
        for tag in soup.find_all(True):
            if tag.name == 'script' and tag.get('src') != base + '/archive-assets/archive.js':
                errors.append(f'{file}: unexpected executable script')
            if tag.name in ('iframe', 'object', 'embed', 'applet') and str(tag) not in original_players:
                errors.append(f'{file}: embed differs from original video players')
            if any(attr.lower().startswith('on') for attr in tag.attrs):
                errors.append(f'{file}: inline event handler')
            if tag.get('id') and re.fullmatch(r'comment-\d+', tag['id']):
                comment_ids.add(int(tag['id'].split('-')[-1]))
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
        content_checks += 1
    missing_comments = {row['id'] for row in data['comments']} - comment_ids
    if missing_comments:
        errors.append(f'{len(missing_comments)} public comments missing from HTML: {sorted(missing_comments)[:20]}')

    for file in site.rglob('*.css'):
        check_css(file.read_text(), file)
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
               'articles_with_video_players': sum(bool(players) for players in expected_videos.values()),
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
