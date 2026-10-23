"""Evidence-backed repairs found by the independent archive comparison."""
from collections import Counter
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re

from bs4 import UnicodeDammit

ROOT = Path(__file__).resolve().parents[1]
SEARCH_PATH = '/archive-search/'


@lru_cache
def repairs():
    return json.loads((ROOT / 'data/audit-repairs.json').read_text())


def decode_document(raw, path=''):
    if isinstance(raw, str):
        return raw
    record = repairs().get('html_sources', {}).get(path)
    if record:
        if hashlib.sha256(raw).hexdigest() != record['capture_sha256']:
            raise ValueError('HTML recovery source changed: ' + path)
        if record.get('file'):
            raw = (ROOT / record['file']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != record['sha256']:
                raise ValueError('HTML recovery checksum differs: ' + path)
        return raw.decode(record['encoding'])
    # The published WordPress pages use UTF-8. Several downloads have obsolete
    # meta declarations; a valid UTF-8 response must not be decoded as Latin-1.
    try:
        return raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        return UnicodeDammit(raw, is_html=True).unicode_markup or ''


def restore_fragments(raw):
    for record in repairs().get('literal_fragments', []):
        raw = raw.replace(record['captured'], record['replacement'])
    return raw


def repair_document(soup):
    for record in repairs().get('unavailable_links', []):
        for link in soup.find_all('a', href=record['href']):
            if link.get_text(' ', strip=True) == record['label']:
                del link['href']
                link['title'] = 'The original link has no recoverable destination.'
                link['data-unavailable-link'] = record['href']
    for paragraph in soup.select('.entry p'):
        for record in repairs().get('excerpts', []):
            if paragraph.get_text() == record['captured_text']:
                paragraph.clear()
                paragraph.string = record['text']

    # Keep the original response target, including on pages with no comments.
    if not soup.find(id='comments'):
        target = soup.select_one('ol.commentlist, .nocomments, #respond')
        if target:
            if target.get('id'):
                target.insert_before(soup.new_tag('span', id='comments'))
            else:
                target['id'] = 'comments'

    # Preserve the first public fragment. Namespace subsequent form controls and
    # their labels, and retain CSS classes for the theme's original form rules.
    for form in soup.select('.archive-form[id="commentform"]'):
        form['class'] = [*form.get('class', []), 'archive-commentform']
        for button in form.select('[id="submit"]'):
            button['class'] = [*button.get('class', []), 'archive-comment-submit']
    used = {tag['id'] for tag in soup.select('[id]')}
    counts = Counter()
    for tag in soup.select('[id]'):
        old = tag['id']
        counts[old] += 1
        if counts[old] == 1:
            continue
        suffix = counts[old]
        new = f'{old}-archive-{suffix}'
        while new in used:
            suffix += 1
            new = f'{old}-archive-{suffix}'
        used.add(new)
        tag['id'] = new
        group = tag.find_parent(class_='archive-form')
        if group:
            for label in group.find_all('label', attrs={'for': old}):
                label['for'] = new
        for style in soup.find_all('style'):
            # Retain any document-local styling of duplicated IDs.
            style.string = re.sub(r'#' + re.escape(old) + r'(?![\w-])',
                                  f':is(#{old}, #{new})', style.decode_contents())
    # Every generated HTML file is emitted as UTF-8, including old downloads.
    for meta in soup.select('meta[charset], meta[http-equiv]'):
        if meta.has_attr('charset'):
            meta['charset'] = 'utf-8'
        elif meta.get('http-equiv', '').lower() == 'content-type':
            meta['content'] = 'text/html; charset=utf-8'
    has_charset = soup.select_one('meta[charset]') or any(
        m.get('http-equiv', '').lower() == 'content-type' for m in soup.find_all('meta'))
    if soup.head and soup.title and not has_charset:
        soup.head.insert(0, soup.new_tag('meta', charset='utf-8'))
    return soup
