"""Explicit repairs for published legacy UI and local Technorati tag indexes."""
from functools import lru_cache
import hashlib
import html
import json
from pathlib import Path
import re
from urllib.parse import quote, unquote_plus, urlsplit

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]


@lru_cache
def ui_repairs():
    return json.loads((ROOT / 'data/ui-repairs.json').read_text())


def text_key(tag):
    return ' '.join(tag.get_text(' ', strip=True).split())


def restore_literal_markup(raw):
    for row in ui_repairs()['literal_markup']:
        before, after = row['captured'], row['replacement']
        if isinstance(raw, bytes):
            before, after = before.encode(), after.encode()
        raw = raw.replace(before, after)
    return raw


def restore_article_ui(soup, path=''):
    repairs = ui_repairs()
    paragraphs = {row['captured_text']: row for row in repairs['paragraph_code']}
    for tag in soup.find_all('p'):
        row = paragraphs.get(text_key(tag))
        if row is None or tag.find_parent(['pre', 'code']):
            continue
        pre = soup.new_tag('pre', attrs={'class': 'archive-code', 'data-repair-code': row['id']})
        code = soup.new_tag('code')
        code.string = row['code']
        pre.append(code)
        if row.get('prefix'):
            prefix = soup.new_tag('p')
            prefix.string = row['prefix']
            tag.insert_before(prefix)
        tag.replace_with(pre)
    literals = {row['captured']: row['replacement'] for row in repairs['literal_markup']}
    for tag in soup.find_all('object'):
        replacement = literals.get(str(tag))
        if replacement:
            fragment = BeautifulSoup(replacement, 'html.parser')
            tag.replace_with(*list(fragment.contents))
    audio = repairs.get('audio', {})
    if audio.get('path'):
        def player():
            element = soup.new_tag('audio', controls='', preload='none', src=audio['path'])
            element['aria-label'] = 'Copenhagen Ruby Brigade podcast'
            return element

        for item in soup.find_all('li', string=audio['captured_label']):
            item.clear()
            link = soup.new_tag('a', href=audio['path'])
            link.string = audio['label']
            item.append(link)
            item.append(soup.new_tag('br'))
            item.append(player())
        if path in audio.get('transcripts', []) and not soup.find('audio'):
            heading = soup.find('h3')
            if heading:
                heading.insert_after(player())


def restore_bookmarklets(soup, path):
    for record in ui_repairs()['bookmarklets'].get(path, []):
        # The capture's broken UTF-16 cookie-editor URL is matched by its label.
        for link in soup.find_all('a'):
            if link.get_text(strip=True) == record['label'] and link.get('href') == record['captured']:
                link['href'] = record['replacement']
                link['data-archive-bookmarklet'] = record['id']


def allowed_bookmarklet(tag, path):
    return any(tag.get('data-archive-bookmarklet') == record['id']
               and tag.get('href') == record['replacement']
               for record in ui_repairs()['bookmarklets'].get(path, []))


def tag_key(url):
    parsed = urlsplit(url)
    if parsed.hostname not in ('technorati.com', 'www.technorati.com') or not parsed.path.startswith('/tag/'):
        return None
    return ' '.join(unquote_plus(parsed.path[5:]).split()).casefold()


@lru_cache
def topic_index():
    """Index historical article tags separately from WordPress's newer taxonomy.

    Original WordPress tag archives and their RSS membership remain intact.
    """
    data = json.loads((ROOT / 'data/content.json').read_text())
    recovery = json.loads((ROOT / 'data/recovery.json').read_text())
    records = {}
    used_paths = set()
    for row in data['posts'] + data['pages']:
        soup = BeautifulSoup(row['content']['rendered'], 'html.parser')
        names = [(tag_key(link['href']), link.get_text(strip=True))
                 for link in soup.select('a[href]') if tag_key(link['href'])]
        for repaired in recovery['tag_lists']:
            if repaired['post_id'] == row['id']:
                names.extend((' '.join(name.split()).casefold(), name) for name in repaired['tags'])
        for key, name in names:
            if key not in records:
                slug = re.sub(r'[^\w.-]+', '-', key).strip('-.') or 'tag'
                path = '/topics/' + quote(slug, safe='-._') + '/'
                if path in used_paths:
                    path = path[:-1] + '-' + hashlib.sha256(key.encode()).hexdigest()[:6] + '/'
                used_paths.add(path)
                records[key] = {'name': name.strip(), 'path': path, 'posts': {}}
            records[key]['posts'][row['id']] = row
    for record in records.values():
        record['posts'] = sorted(record['posts'].values(), key=lambda row: row['date'], reverse=True)
    return records


def topic_body(record):
    items = []
    for row in record['posts']:
        path = urlsplit(row['link']).path
        title = BeautifulSoup(row['title']['rendered'], 'html.parser').get_text()
        items.append('<li><a href="' + html.escape(path, quote=True) + '">' + html.escape(title)
                     + '</a> <small>' + row['date'][:10] + '</small></li>')
    return '<ul class="archive-topic-posts">' + ''.join(items) + '</ul>'
