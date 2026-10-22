#!/usr/bin/env python3
"""Capture the public WordPress site and build an offline static archive.

Only GET requests are used. Raw responses stay in .cache; only explicitly
selected public API fields and sanitized static documents are published.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import time
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, quote, unquote, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, Comment
from recovery import recovery_data, restore_code, restore_gists, restore_demos, UNDO_URL, UNDO_PATH

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache'
SITE = ROOT / 'site'
ORIGIN = 'http://justaddwater.dk'
HOSTS = {'justaddwater.dk', 'www.justaddwater.dk'}
ASSET_SUFFIXES = {'.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp',
                  '.ico', '.pdf', '.zip', '.gz', '.txt', '.xml', '.mp3', '.mp4',
                  '.mov', '.woff', '.woff2', '.ttf', '.eot', '.swf', '.doc', '.xls'}
BLOCKED = ('/wp-admin', '/wp-json', '/wp-login', '/wp-comments-post', '/xmlrpc', '/wp-cron')
CSS_URL = re.compile(r'url\(\s*([\'\"]?)(.*?)\1\s*\)', re.I)
# Player endpoints present in the original articles, including retired services.
VIDEO_PLAYERS = {
    'www.youtube.com': ('/embed/', '/v/'),
    'player.vimeo.com': ('/video/',),
    'video.google.com': ('/googleplayer.swf',),
    'blip.tv': ('/scripts/flash/showplayer.swf',),
    'mojiti.com': ('/bofangqi/',),
}
COUNTS = {}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def fetch(url):
    """Cache bounded requests, including original response metadata."""
    key = hashlib.sha256(url.encode()).hexdigest()
    body_file, meta_file = CACHE / (key + '.body'), CACHE / (key + '.json')
    if meta_file.exists() and body_file.exists():
        return body_file.read_bytes(), json.loads(meta_file.read_text())
    CACHE.mkdir(exist_ok=True)
    for attempt in range(3):
        try:
            req = Request(url, headers={'User-Agent': 'justaddwater-static-archive/1.0 (owner-requested migration)'})
            with urlopen(req, timeout=30) as response:
                body = response.read(45 * 1024 * 1024 + 1)
                if len(body) > 45 * 1024 * 1024:
                    raise ValueError('Asset exceeds 45 MiB safety bound')
                meta = {'url': url, 'final_url': response.url, 'status': response.status,
                        'headers': dict(response.headers), 'captured_at': datetime.now(timezone.utc).isoformat()}
            body_file.write_bytes(body)
            write_json(meta_file, meta)
            return body, meta
        except HTTPError as error:
            if error.code < 500 or attempt == 2:
                raise
        except (URLError, TimeoutError, ConnectionError):
            if attempt == 2:
                raise
        time.sleep(1 + attempt)


def inventory():
    fields = {
        'posts': ['id', 'date', 'date_gmt', 'modified', 'slug', 'link', 'title', 'content', 'excerpt', 'author', 'categories', 'tags'],
        'pages': ['id', 'date', 'date_gmt', 'modified', 'slug', 'link', 'title', 'content', 'excerpt', 'author', 'parent'],
        'media': ['id', 'date', 'slug', 'link', 'title', 'caption', 'description', 'alt_text', 'source_url', 'mime_type', 'media_details'],
        'comments': ['id', 'post', 'parent', 'date', 'date_gmt', 'author_name', 'author_url', 'content', 'link'],
        'categories': ['id', 'count', 'name', 'slug', 'link', 'description', 'parent'],
        'tags': ['id', 'count', 'name', 'slug', 'link', 'description'],
        'users': ['id', 'name', 'slug', 'link'],
    }
    data = {'source': ORIGIN, 'captured_at': datetime.now(timezone.utc).isoformat(), 'api_reported_totals': {}}
    for kind, allowed in fields.items():
        items, page, total = [], 1, 1
        while page <= total:
            raw, meta = fetch(f'{ORIGIN}/wp-json/wp/v2/{kind}?per_page=100&page={page}')
            rows = json.loads(raw)
            items.extend({key: row[key] for key in allowed if key in row} for row in rows)
            headers = {k.lower(): v for k, v in meta['headers'].items()}
            total = int(headers['x-wp-totalpages'])
            expected = int(headers['x-wp-total'])
            page += 1
        assert len({row['id'] for row in items}) == len(items), f'Duplicate {kind} IDs'
        # Older WordPress versions can count attachments whose parent is not
        # publicly readable, then omit them from the returned collection.
        # Preserve both counts rather than claiming inaccessible items exist.
        data['api_reported_totals'][kind] = expected
        if len(items) != expected:
            print(f'{kind}: API advertises {expected}; returns {len(items)} public records', flush=True)
        data[kind] = items
        print(f'{kind}: {len(items)}', flush=True)
    write_json(ROOT / 'data/content.json', data)
    return data


def load_data():
    return json.loads((ROOT / 'data/content.json').read_text())


def id_routes(data):
    return {str(row['id']): urlsplit(row['link']).path
            for kind in ('posts', 'pages', 'media') for row in data[kind]}


def local_url(value, base, ids):
    value = value.strip() if value else value
    if not value or value.startswith(('data:', 'mailto:', 'tel:', '#')):
        return None
    parts = urlsplit(urljoin(base, html.unescape(value)))
    if parts.hostname not in HOSTS or parts.scheme not in ('http', 'https'):
        return None
    path = re.sub(r'/+', '/', parts.path or '/')
    path = recovery_data()['aliases'].get(unquote(path), path)
    # A few original articles accidentally used a relative uploads path.
    if '/wp-content/' in path and not path.startswith('/wp-content/'):
        path = path[path.index('/wp-content/'):]
    if '\\' in path or any(p == '..' for p in unquote(path).split('/')):
        return None
    if any(path.startswith(p) for p in BLOCKED):
        return None
    if path.rstrip('/').endswith('/trackback'):
        return None
    if path.endswith('/function.file-exists'):
        return None
    query = parse_qs(parts.query)
    for key in ('p', 'page_id', 'attachment_id'):
        if key in query:
            return ids.get(query[key][0])
    if 's' in query:
        return '/search/'
    if 'feed' in query:
        return '/comments/feed/' if query['feed'][0] == 'comments-rss2' else '/feed/'
    if 'paged' in query:
        path = f'{path.rstrip("/")}/page/{query["paged"][0]}/'
    if 'cat' in query or 'm' in query or 'author' in query:
        return None
    if Path(path).suffix.lower() in ('.php', '.asp', '.aspx'):
        if path == '/index.php':
            return '/'
        return None
    if not Path(path).suffix and not path.endswith('/'):
        path += '/'
    return quote(unquote(path), safe="/!$&'()*+,-.;=@_~")


def disk_path(path):
    plain = unquote(urlsplit(path).path)
    relative = plain.lstrip('/')
    if plain.endswith('/') or not Path(plain).suffix:
        relative = relative.rstrip('/') + '/index.html' if relative else 'index.html'
    result = SITE / relative
    if not result.resolve().is_relative_to(SITE.resolve()):
        raise ValueError(f'Unsafe output path: {path}')
    return result


def is_asset(path):
    return Path(urlsplit(path).path).suffix.lower() in ASSET_SUFFIXES or path.startswith(('/wp-content/', '/wp-includes/'))


def is_feed(path):
    return bool(re.search(r'/(?:feed|rss2?|atom)/?$', path))


def embedded_css(soup):
    """Include both style attributes and WordPress's per-template style blocks."""
    yield from (tag['style'] for tag in soup.find_all(style=True))
    yield from (tag.string or '' for tag in soup.find_all('style'))


def parse_document(raw, path='', recover=True):
    # Match the browser's HTML5 tree construction. Legacy WordPress sometimes
    # lets formatting tags cross paragraph boundaries; html.parser closes them
    # early and silently changes how the published article looks.
    if recover:
        raw = restore_code(raw)
    return BeautifulSoup(protect_form_examples(raw), 'html5lib')


def protect_form_examples(raw):
    """Keep form tags in legacy [code] snippets from consuming article prose."""
    blocks = r'(\[code\b[^\]]*\])(.*?)(\[/code\])'
    forms = r'''</?form\b(?:"[^"]*"|'[^']*'|[^'">])*>'''
    binary = isinstance(raw, bytes)
    if binary:
        blocks, forms = blocks.encode(), forms.encode()

    def escape_tag(match):
        tag = match[0]
        # Preserve the capture's original byte encoding; only ASCII markup is
        # escaped. Ordinary forms outside code blocks are handled as before.
        if binary:
            return tag.replace(b'&', b'&amp;').replace(b'<', b'&lt;').replace(b'>', b'&gt;')
        return html.escape(tag, quote=False)

    return re.sub(blocks, lambda block: block[1] + re.sub(forms, escape_tag, block[2], flags=re.I) + block[3],
                  raw, flags=re.I | re.S)


def references(soup, base, ids):
    pages, assets = set(), set()
    for tag in soup.find_all(['a', 'img', 'link', 'source', 'video', 'audio', 'object', 'embed']):
        attrs = ['href'] if tag.name in ('a', 'link') else ['src', 'poster', 'data']
        for attr in attrs:
            val = tag.get(attr)
            if not val:
                continue
            path = local_url(val, base, ids)
            if not path:
                continue
            if is_asset(path):
                assets.add(path)
            elif tag.name == 'a' and not is_feed(path):
                # Comment authors and historical links may point anywhere; these
                # aren't navigation and do not expand the crawl.
                if not tag.find_parent(class_='commentlist'):
                    pages.add(path)
        if tag.get('srcset'):
            for item in tag['srcset'].split(','):
                path = local_url(item.strip().split()[0], base, ids) if item.strip() else None
                if path:
                    assets.add(path)
    for css in embedded_css(soup):
        for match in CSS_URL.finditer(css):
            path = local_url(match[2], base, ids)
            if path:
                assets.add(path)
    return pages, assets


def crawl(data):
    ids = id_routes(data)
    pages = {'/', '/archive/'}
    for kind in ('posts', 'pages', 'media', 'categories', 'tags', 'users', 'comments'):
        pages.update(local_url(row['link'], ORIGIN, ids) for row in data[kind]
                     if row.get('link') and row.get('count', 1) > 0)
    for post in data['posts']:
        year, month = post['date'][:7].split('-')
        pages.update((f'/{year}/', f'/{year}/{month}/'))
    pages.discard(None)
    assets = set()
    for media in data['media']:
        path = local_url(media.get('source_url'), ORIGIN, ids)
        if path:
            assets.add(path)
        for size in media.get('media_details', {}).get('sizes', {}).values():
            path = local_url(size.get('source_url'), ORIGIN, ids)
            if path:
                assets.add(path)
    done, captured, failed = set(), {}, {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        while pages - done:
            batch = sorted(pages - done)
            if len(pages) > 6000:
                raise RuntimeError('Crawl exceeded the 6000-page bound; inspect navigation')
            futures = {pool.submit(fetch, ORIGIN + path): path for path in batch}
            for future in as_completed(futures):
                path = futures[future]
                done.add(path)
                try:
                    body, meta = future.result()
                    if urlsplit(meta['final_url']).hostname not in HOSTS:
                        raise ValueError('External redirect')
                    if 'text/html' not in next((v for k, v in meta['headers'].items() if k.lower() == 'content-type'), ''):
                        assets.add(path)
                        continue
                    soup = BeautifulSoup(body, 'html.parser')
                    new_pages, new_assets = references(soup, ORIGIN + path, ids)
                    pages.update(p for p in new_pages if not is_asset(p))
                    assets.update(new_assets)
                    captured[path] = meta['final_url']
                except Exception as error:
                    failed[path] = str(error)
                if len(done) % 100 == 0:
                    print(f'HTML: {len(done)} fetched / {len(pages)} discovered; {len(failed)} unavailable', flush=True)
            write_json(CACHE / 'crawl.json', {'pages': captured, 'assets': sorted(assets), 'failed': failed})
    downloaded, unavailable = {}, {}
    pending = assets.copy()
    with ThreadPoolExecutor(max_workers=4) as pool:
        while pending:
            futures = {pool.submit(fetch, ORIGIN + path): path for path in sorted(pending)}
            pending = set()
            for future in as_completed(futures):
                path = futures[future]
                try:
                    body, meta = future.result()
                    if urlsplit(meta['final_url']).hostname not in HOSTS:
                        raise ValueError('External redirect')
                    downloaded[path] = meta['final_url']
                    dependencies = set()
                    if path.endswith('.css'):
                        for match in CSS_URL.finditer(body.decode('utf-8', 'replace')):
                            extra = local_url(match[2], ORIGIN + path, ids)
                            if extra:
                                dependencies.add(extra)
                    elif 'text/html' in next((v for k, v in meta['headers'].items() if k.lower() == 'content-type'), ''):
                        # Downloadable HTML demos have their own inline CSS and
                        # images, even though they aren't WordPress page routes.
                        _, dependencies = references(BeautifulSoup(body, 'html.parser'), ORIGIN + path, ids)
                    pending.update(dependencies - assets)
                    assets.update(dependencies)
                except Exception as error:
                    unavailable[path] = str(error)
                if (len(downloaded) + len(unavailable)) % 100 == 0:
                    print(f'Assets: {len(downloaded)} saved; {len(unavailable)} unavailable', flush=True)
    state = {'pages': captured, 'assets': downloaded, 'failed_pages': failed, 'failed_assets': unavailable}
    write_json(CACHE / 'capture.json', state)
    return state


def is_video_embed(tag):
    if tag.name not in ('iframe', 'object', 'embed'):
        return False
    urls = [tag.get('src', ''), tag.get('data', '')]
    if tag.name == 'object':
        urls.extend(param.get('value', '') for param in tag.find_all('param')
                    if param.get('name', '').lower() == 'movie')
    for url in urls:
        parts = urlsplit(url)
        if parts.scheme in ('http', 'https') and parts.path.startswith(VIDEO_PLAYERS.get(parts.hostname, ())):
            return True
    return False


def archive_form(soup, form):
    """Keep the original controls visible without a form that can submit."""
    # Hidden submission metadata and anti-spam fields have no archival UI.
    for node in reversed(form.select('input[type="hidden"], [hidden], [style]')):
        if node.get('type') == 'hidden' or node.has_attr('hidden') or re.search(r'display\s*:\s*none\b', node.get('style', ''), re.I):
            node.decompose()

    form.name = 'div'
    form['class'] = [*form.get('class', []), 'archive-form']
    form['role'] = 'group'
    form['aria-disabled'] = 'true'
    for attr in ('action', 'method', 'enctype', 'target', 'accept-charset', 'autocomplete', 'novalidate'):
        form.attrs.pop(attr, None)
    for control in form.find_all(['input', 'textarea', 'select', 'button', 'fieldset', 'option', 'optgroup']):
        control['disabled'] = ''
        for attr in ('form', 'formaction', 'formmethod', 'formenctype', 'formtarget', 'formnovalidate', 'autofocus', 'tabindex'):
            control.attrs.pop(attr, None)
    for editable in form.select('[contenteditable]'):
        editable['contenteditable'] = 'false'

    number = 1
    while soup.find(id=f'archive-form-notice-{number}'):
        number += 1
    notice_id = f'archive-form-notice-{number}'
    form['aria-describedby'] = ' '.join(filter(None, [form.get('aria-describedby'), notice_id]))
    note = soup.new_tag('p', attrs={'class': 'archive-form-notice', 'id': notice_id, 'role': 'note'})
    heading = soup.new_tag('strong')
    heading.string = 'This form no longer accepts submissions.'
    note.append(heading)
    form.insert_before(note)


def clean_html(soup, path=''):
    restore_gists(soup)
    # The old host prints PHP open_basedir warnings on attachment pages. These
    # are runtime diagnostics, not article content or archive navigation.
    for warning in soup.find_all('b', string=re.compile(r'^(Warning|Notice|Deprecated)$')):
        following = ''.join(str(x) for x in list(warning.next_siblings)[:12])
        if 'open_basedir' in following and '/home/' in following:
            node = warning.next_sibling
            warning.extract()
            while node is not None:
                after = node.next_sibling
                stop = getattr(node, 'name', None) == 'br'
                node.extract()
                if stop:
                    break
                node = after
    # Keep original video players, even obsolete Flash players. Process nested
    # embeds before their objects so removing a parent cannot invalidate a child.
    for tag in reversed(soup.find_all(['script', 'iframe', 'object', 'embed', 'applet', 'base'])):
        if not is_video_embed(tag) and not (tag.name == 'iframe' and tag.get('src') == UNDO_URL):
            tag.decompose()
    for comment in soup.find_all(string=lambda x: isinstance(x, Comment)):
        comment.extract()
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr.lower().startswith('on') or attr.lower() in ('srcdoc', 'ping'):
                del tag[attr]
        for attr in ('href', 'src', 'action', 'xlink:href'):
            if str(tag.get(attr, '')).strip().lower().startswith(('javascript:', 'vbscript:')):
                del tag[attr]
    for tag in soup.select('link[rel="pingback"], link[rel="https://api.w.org/"], link[rel="EditURI"], link[rel="wlwmanifest"]'):
        tag.decompose()
    for form in soup.find_all('form'):
        if form.find('input', attrs={'name': 's'}):
            form['action'] = '/search/'
            form['method'] = 'get'
        else:
            archive_form(soup, form)
    for tag in soup.select('.comment-reply-link, #cancel-comment-reply-link'):
        tag.decompose()
    for tag in soup.find_all('a', href=True):
        if urlsplit(tag['href']).path.rstrip('/').endswith('/trackback'):
            del tag['href']
        elif tag['href'].endswith('#respond'):
            tag['href'] = tag['href'].removesuffix('#respond') + '#comments'
    restore_demos(soup, path)
    return soup


def rewrite_css(css, base, ids, routes, unavailable, external):
    def replace(match):
        value = match[2]
        path = local_url(value, base, ids)
        if path:
            if path in routes:
                return 'url("' + path + '")'
            unavailable.add(path)
            # A missing background should leave the original background color
            # visible, rather than tile an image-placeholder message.
            return 'none'
        if urlsplit(urljoin(base, value)).hostname not in HOSTS and not value.startswith(('data:', '#')):
            image = external.get(value, {})
            return 'url("' + image['path'] + '")' if image.get('path') else 'none'
        return match[0]
    return CSS_URL.sub(replace, css)


def rewrite(soup, base, ids, routes, unavailable, external=None):
    external = external or {}
    for tag in soup.find_all(True):
        for attr in ('href', 'src', 'poster', 'data', 'action'):
            value = tag.get(attr)
            if not value:
                continue
            if attr == 'href' and re.match(r'^(?:www\.|github\.com/)', value):
                value = 'https://' + value
                tag[attr] = value
            elif attr == 'href' and value.startswith('http:www.'):
                value = value.replace('http:', 'http://', 1)
                tag[attr] = value
            if tag.name == 'img' and attr == 'src' and urlsplit(value).hostname and urlsplit(value).hostname not in HOSTS:
                image = external.get(value, {})
                tag['src'] = '/archive-assets/feed.svg' if value.endswith('/feed-icon32x32.png') else image.get('path', '/archive-assets/unavailable.svg')
                if value.endswith('/feed-icon32x32.png'):
                    tag['alt'] = 'RSS feed'
                tag['data-original-url'] = value
                continue
            if attr == 'href' and urlsplit(value).hostname == 'feeds.justaddwater.dk':
                tag[attr] = '/feed/index.xml'
                continue
            path = local_url(value, base, ids)
            if not path:
                if attr == 'href' and any(urlsplit(urljoin(base, value)).path.startswith(p) for p in BLOCKED) and urlsplit(urljoin(base, value)).hostname in HOSTS:
                    del tag[attr]
                continue
            fragment = urlsplit(html.unescape(value)).fragment
            if is_feed(path):
                path = '/comments/feed/' if '/comments/' in path else '/feed/'
                tag[attr] = path + 'index.xml'
                continue
            if path in routes or path in ('/search/', '/feed/', '/comments/feed/'):
                tag[attr] = path + ('#' + fragment if fragment else '')
            else:
                # Preserve already-broken historical references as links to a
                # local explanation; record the source for future recovery.
                unavailable.add(path)
                if attr in ('src', 'poster') and tag.name in ('img', 'source', 'video'):
                    tag[attr] = '/archive-assets/unavailable.svg'
                    tag['data-original-url'] = ORIGIN + path
                elif attr == 'href' and tag.name == 'a':
                    tag[attr] = '/unavailable/?url=' + quote(path, safe='')
                    tag['data-original-url'] = ORIGIN + path
                else:
                    del tag[attr]
        if tag.get('srcset'):
            entries = []
            for item in tag['srcset'].split(','):
                parts = item.strip().split()
                if parts:
                    path = local_url(parts[0], base, ids)
                    if path in routes:
                        entries.append(' '.join([path, *parts[1:]]))
            if entries:
                tag['srcset'] = ', '.join(entries)
            else:
                del tag['srcset']
        if tag.get('style'):
            tag['style'] = rewrite_css(tag['style'], base, ids, routes, unavailable, external)
        if tag.name == 'style':
            tag.string = rewrite_css(tag.string or '', base, ids, routes, unavailable, external)
    for tag in soup.select('link[rel="canonical"], link[rel="shortlink"]'):
        if tag.get('href', '').startswith('/'):
            tag['href'] = 'https://justaddwater.dk' + tag['href']
    if soup.head:
        css = soup.new_tag('link', rel='stylesheet', href='/archive-assets/archive.css')
        soup.head.append(css)
        script = soup.new_tag('script', src='/archive-assets/archive.js', defer='defer')
        soup.head.append(script)
    return soup


def generated_page(template, title, body):
    soup = parse_document(template)
    content = soup.select_one('#content')
    content.clear()
    content.append(BeautifulSoup(f'<h2>{html.escape(title)}</h2>{body}', 'html.parser'))
    soup.title.string = title + ' | justaddwater.dk'
    for link in soup.select('link[rel="canonical"], link[rel="shortlink"]'):
        link.decompose()
    return str(soup)


def build(data, state):
    recovery = recovery_data()
    recovered_assets = {}
    for asset in recovery['assets']:
        raw = (ROOT / asset['file']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != asset['sha256']:
            raise ValueError('Recovered asset checksum differs: ' + asset['path'])
        recovered_assets[quote(asset['path'], safe="/!$&'()*+,-.;=@_~")] = raw
    # Clear generated files so removed crawl routes don't survive a rebuild.
    # Archive controls and recovered external images are maintained separately.
    SITE.mkdir(exist_ok=True)
    for child in SITE.iterdir():
        if child.name not in ('archive-assets', 'CNAME'):
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    ids = id_routes(data)
    routes = set(state['pages']) | set(state['assets']) | set(recovered_assets) | {UNDO_PATH, '/archive-assets/demos.js'}
    external_file = ROOT / 'data/external-images.json'
    external = json.loads(external_file.read_text()) if external_file.exists() else {}
    unavailable, comment_ids = set(), set()
    for path in sorted(state['pages']):
        raw, _ = fetch(ORIGIN + path)
        soup = clean_html(parse_document(raw, path=path), path=path)
        soup = rewrite(soup, ORIGIN + path, ids, routes, unavailable, external)
        for tag in soup.find_all(id=re.compile(r'^comment-\d+$')):
            comment_ids.add(int(tag['id'].split('-')[-1]))
        target = disk_path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(str(soup))
    for path in sorted(state['assets']):
        if is_feed(path):
            continue
        raw, meta = fetch(ORIGIN + path)
        content_type = next((v for k, v in meta['headers'].items() if k.lower() == 'content-type'), '')
        if 'text/html' in content_type:
            raw = str(rewrite(clean_html(parse_document(raw), path=path), ORIGIN + path, ids, routes, unavailable, external)).encode()
        elif path.endswith('.css'):
            text = raw.decode('utf-8', 'replace')
            raw = rewrite_css(text, ORIGIN + path, ids, routes, unavailable, external).encode()
        # JavaScript examples can be downloaded, but aren't executed by pages.
        if path.endswith('.php'):
            continue
        target = disk_path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    for path, raw in recovered_assets.items():
        target = disk_path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    for alias, canonical in recovery['aliases'].items():
        target = disk_path(alias)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(disk_path(canonical), target)
    template = (SITE / 'index.html').read_text()
    for path, title, content in [
        ('/search/', 'Search the archive', '<form action="/search/" method="get"><label for="archive-query">Search posts and pages</label> <input id="archive-query" name="s" type="search"/><button type="submit">Search</button></form><p id="search-status" role="status"></p><ol id="search-results"></ol>'),
        ('/unavailable/', 'Unavailable in the original site', '<p>This historical link was already unavailable when the blog was archived. The rest of the archive is preserved.</p><p><a href="/archive/">Browse the archive</a> or <a href="/search/">search posts</a>.</p>'),
        ('/404.html', 'Page not found', '<p>This address is not in the archive.</p><p><a href="/archive/">Browse all posts</a> or <a href="/search/">search the archive</a>.</p>'),
    ]:
        target = disk_path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(generated_page(template, title, content))
    search = [{'id': p['id'], 'url': urlsplit(p['link']).path,
               'title': html.unescape(p['title']['rendered']), 'date': p['date'][:10],
               'text': clean_html(parse_document(p['content']['rendered'])).get_text(' ', strip=True)}
              for p in data['posts'] + data['pages']]
    write_json(SITE / 'archive-assets/search.json', search)
    write_json(SITE / 'archive-assets/routes.json', ids)
    feeds(data)
    (SITE / '.nojekyll').touch()
    sitemap = ET.Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for path in sorted({urlsplit(p['link']).path for p in data['posts'] + data['pages']} | {'/'}):
        node = ET.SubElement(sitemap, 'url')
        ET.SubElement(node, 'loc').text = 'https://justaddwater.dk' + path
    ET.ElementTree(sitemap).write(SITE / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
    (SITE / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://justaddwater.dk/sitemap.xml\n')
    missing_comments = sorted({c['id'] for c in data['comments']} - comment_ids)
    report = {'source': ORIGIN, 'captured_at': data['captured_at'],
              'content_counts': {k: len(data[k]) for k in ('posts', 'pages', 'media', 'comments', 'categories', 'tags', 'users')},
              'api_reported_totals': data['api_reported_totals'],
              'html_pages': len(state['pages']), 'downloaded_assets': len(state['assets']),
              'comments_in_html': len(comment_ids), 'comments_missing_from_html': missing_comments,
              'recovered_assets': [a['path'] for a in recovery['assets']],
              'repaired_asset_aliases': recovery['aliases'],
              'recovered_code_blocks': len(recovery['code_blocks']),
              'recovered_gist_embeds': len(recovery['gists']),
              'unavailable_pages': {p: e for p, e in state['failed_pages'].items() if local_url(p, ORIGIN, ids) and local_url(p, ORIGIN, ids) not in routes},
              'unavailable_assets': {p: e for p, e in state['failed_assets'].items() if local_url(p, ORIGIN, ids) not in routes},
              'unavailable_references': sorted(unavailable)}
    write_json(ROOT / 'data/capture-report.json', report)
    print(json.dumps({k: v for k, v in report.items() if not isinstance(v, (list, dict))}, indent=2))
    print('Comments missing from rendered HTML:', len(missing_comments), flush=True)


def feeds(data):
    for kind, path in [('posts', '/feed/'), ('comments', '/comments/feed/')]:
        rss = ET.Element('rss', version='2.0')
        channel = ET.SubElement(rss, 'channel')
        ET.SubElement(channel, 'title').text = 'justaddwater.dk' + (' comments' if kind == 'comments' else '')
        ET.SubElement(channel, 'link').text = 'https://justaddwater.dk/'
        ET.SubElement(channel, 'description').text = 'Instant Usability & Web Standards — static archive'
        for row in data[kind][:50]:
            item = ET.SubElement(channel, 'item')
            title = row['title']['rendered'] if kind == 'posts' else 'Comment by ' + row['author_name']
            ET.SubElement(item, 'title').text = html.unescape(title)
            ET.SubElement(item, 'link').text = row['link'].replace('http://', 'https://', 1)
            ET.SubElement(item, 'guid').text = row['link']
            content = BeautifulSoup(restore_code(row['content']['rendered']), 'html.parser')
            restore_gists(content)
            for tag in content.find_all(['script', 'iframe', 'object', 'embed']):
                tag.decompose()
            ET.SubElement(item, 'description').text = str(content)
            date = datetime.fromisoformat(row.get('date_gmt') or row['date']).replace(tzinfo=timezone.utc)
            ET.SubElement(item, 'pubDate').text = date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        target = disk_path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        # index.xml is requested explicitly by archive links and served as XML.
        ET.ElementTree(rss).write(target.with_name('index.xml'), encoding='utf-8', xml_declaration=True)
        target.write_text('<!doctype html><meta http-equiv="refresh" content="0;url=index.xml"><a href="index.xml">RSS feed</a>')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['inventory', 'capture', 'build', 'all'])
    args = parser.parse_args()
    if args.command in ('inventory', 'all'):
        data = inventory()
    else:
        data = load_data()
    if args.command in ('capture', 'all'):
        state = crawl(data)
    if args.command in ('build', 'all'):
        state = json.loads((CACHE / 'capture.json').read_text())
        build(data, state)
