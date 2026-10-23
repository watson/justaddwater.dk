#!/usr/bin/env python3
"""Compare the capture with the archive, independently of the converter.

No archive/recovery/legacy imports: expectations come from recorded evidence.
The cache is read-only. Reports, live snapshots and screenshots stay outside site/.
"""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from functools import lru_cache
import difflib
import hashlib
import html
from html.parser import HTMLParser
import json
import mimetypes
from pathlib import Path
import re
import subprocess
import sys
import textwrap
from urllib.parse import parse_qs, unquote, urldefrag, urljoin, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, UnicodeDammit

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'http://justaddwater.dk'
HOSTS = {'justaddwater.dk', 'www.justaddwater.dk'}
POLICY_VERSION = 2


def read_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def normalize_space(value):
    return ' '.join(value.split())


def local_file(site, path):
    """Resolve encoded URL paths, including directory feeds, without traversal."""
    target = (site / unquote(urlsplit(path).path).lstrip('/')).resolve()
    if not target.is_relative_to(site.resolve()):
        return None
    if target.is_dir():
        for name in ('index.html', 'index.xml'):
            if (target / name).is_file():
                return target / name
        return None
    return target if target.is_file() else None


def canonical(url, base=ORIGIN + '/', prefix=''):
    value = urlsplit(urljoin(base, html.unescape(url)))
    path = unquote(value.path) or '/'
    if value.hostname == 'archive.test' or value.hostname == 'watson.github.io':
        if prefix and (path == prefix or path.startswith(prefix + '/')):
            path = path[len(prefix):] or '/'
        elif value.hostname == 'watson.github.io' and path.startswith('/justaddwater.dk/'):
            path = path[len('/justaddwater.dk'):]
        host = ''
    else:
        host = '' if value.hostname in HOSTS else value.netloc.lower()
    # Version query strings on local dependencies do not change their file.
    query = value.query if host or value.query and not re.fullmatch(r'ver=[^&]*', value.query) else ''
    return (value.scheme + '://' + host if host else '') + path + ('?' + query if query else '') + ('#' + unquote(value.fragment) if value.fragment else '')


def visible_text(soup):
    copy = BeautifulSoup(str(soup), 'html.parser')
    for node in copy.select('script, style, template, head, title, input[type=hidden]'):
        node.decompose()
    return normalize_space(copy.get_text(' ', strip=True))


@lru_cache(maxsize=4096)
def fragment_ids(path):
    class Anchors(HTMLParser):
        def __init__(self):
            super().__init__()
            self.ids = set()

        def handle_starttag(self, tag, attrs):
            self.ids.update(value for key, value in attrs if value and (key == 'id' or tag == 'a' and key == 'name'))
    parser = Anchors()
    parser.feed(path.read_text(errors='replace'))
    return parser.ids


def text_changes(before, after):
    a, b = before.split(), after.split()
    result = []
    for tag, i, j, k, l in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != 'equal':
            result.append({'kind': tag, 'before': ' '.join(a[i:j]), 'after': ' '.join(b[k:l]),
                           'context': ' '.join(a[max(0, i - 10):i])})
    return result


def finding(kind, status, message, **evidence):
    return {'kind': kind, 'status': status, 'message': message, **evidence}


def inline_review(scripts):
    akismet = re.compile(r'document\.getElementById\(\s*"ak_js_\d+"\s*\)\.setAttribute\(\s*"value",\s*\(\s*new Date\(\)\s*\)\.getTime\(\)\s*\);')
    return [s for s in scripts if not any(marker in s for marker in ('mmposts', 'mmcomments', 'urchinTracker', '_wpemojiSettings', '_gaq')) and not akismet.fullmatch(s.strip())]


def switched_links(before, after):
    old = {(r['label'], r['url']) for r in before if r['tag'] == 'a' and r['label']}
    new = {(r['label'], r['url']) for r in after if r['tag'] == 'a' and r['label']}
    labels, urls = {label for label, _ in new}, {url for _, url in new}
    return [{'label': label, 'original_url': url, 'new_urls': sorted(u for text, u in new if text == label)}
            for label, url in sorted(old - new) if label in labels and url in urls]


class Expectations:
    """Narrow, documented exceptions; no whole-page ignore lists."""
    def __init__(self, root, cache=None):
        self.recovery = read_json(root / 'data/recovery.json', {})
        self.ui = read_json(root / 'data/ui-repairs.json', {})
        self.repairs = read_json(root / 'data/audit-repairs.json', {})
        self.root = root
        self.videos = read_json(root / 'data/video-players.json', [])
        self.images = read_json(root / 'data/external-images.json', {})
        content = read_json(root / 'data/content.json', {})
        self.ids = {str(r['id']): canonical(r['link']) for key in ('posts', 'pages', 'media') for r in content.get(key, [])}
        self.player_urls = {v['url'] for video in self.videos for v in refs(BeautifulSoup(video['captured'], 'html.parser'), ORIGIN + '/')}
        self.capture_aliases = {}
        self.failed_paths = set()
        self.source_files = {}
        if cache:
            inventory = read_json(cache / 'capture.json', {})
            inventory['pages'] = inventory.get('pages', {}) | read_json(root / 'data/supplemental-capture.json', {}).get('pages', {})
            self.failed_paths = {canonical(p) for k in ('failed_pages', 'failed_assets') for p in inventory.get(k, {})}
            for kind in ('pages', 'assets'):
                for path, url in inventory.get(kind, {}).items():
                    body, meta = snapshot(cache, url)
                    if body:
                        self.source_files[canonical(url)] = body
                        self.source_files[canonical(ORIGIN + path)] = body
                    final = canonical(meta.get('final_url', url))
                    if canonical(ORIGIN + path) != final:
                        self.capture_aliases[canonical(ORIGIN + path)] = final

    def reference_issues(self, removed, added, path, raw=''):
        """Explain known URL migrations; retain every other changed target."""
        problems, explained = [], []
        mappings = {canonical(k): canonical(v) for k, v in self.ui.get('external_link_repairs', {}).items()}
        mappings.update(self.capture_aliases)
        mappings.update({canonical(k): canonical(v) for k, v in self.repairs.get('reference_mappings', {}).items()})
        mappings.update(self.repairs.get('scoped_links', {}).get(path, {}))
        mappings.update({'http://feeds.justaddwater.dk/jaw/posts': '/feed/', 'http://feeds.feedburner.com/jaw/posts': '/feed/',
                         'http://feeds.justaddwater.dk/jaw/comments': '/comments/feed/'})
        for group in (self.recovery.get('aliases', {}), self.ui.get('redirects', {}), self.repairs.get('redirects', {})):
            mappings.update({canonical(k): canonical(v) for k, v in group.items()})
        mappings.update({canonical(k): v['path'] for k, v in self.images.items() if v.get('path')})
        mappings.update({canonical(d['source_url']): d['local_path'] for d in self.recovery.get('demos', []) if d.get('source_url') and d.get('local_path')})
        added_keys = {(v['tag'], v['attribute'], v['url']) for v in added}
        slash_keys = {(tag, attr, url.rstrip('/')) for tag, attr, url in added_keys}
        code_refs = set()
        for block in self.recovery.get('code_blocks', []):
            if block['captured'] in raw:
                code_refs.update((r['tag'], r['attribute'], r['url']) for r in refs(BeautifulSoup(block['captured'], 'html.parser'), ORIGIN + path))
        for ref in removed:
            url = ref['url']
            parsed = urlsplit(url)
            reason = None
            replacement = mappings.get(url)
            query = parse_qs(parsed.query)
            post_id = (query.get('p') or query.get('page_id') or query.get('attachment_id') or [None])[0]
            if not parsed.netloc and post_id in self.ids:
                replacement = self.ids[post_id] + ('feed/' if query.get('feed') or parsed.path == '/feed/' else '') + ('#' + parsed.fragment if parsed.fragment else '')
            if not parsed.netloc and query.get('s'):
                replacement = '/archive-search/?' + parsed.query
            if replacement and (ref['tag'], ref['attribute'], replacement) in added_keys:
                reason = 'recorded URL or recovered resource'
            elif (ref['tag'], ref['attribute'], url) in code_refs:
                reason = 'literal dependency inside a restored code example'
            elif url in self.repairs.get('unavailable_references', {}):
                item = self.repairs['unavailable_references'][url]
                if (item.get('replacement') is None or
                        (ref['tag'], ref['attribute'], item.get('replacement')) in added_keys):
                    reason = item['reason']
            elif (ref['tag'], ref['attribute'], url.rstrip('/')) in slash_keys:
                reason = 'directory slash normalization'
            elif ref['tag'] == 'script' and (parsed.path.startswith(('/wp-includes/', '/wp-content/plugins/')) or
                                           parsed.hostname in ('www.google-analytics.com', 'tracker.measuremap.com', 'feeds.feedburner.com') or
                                           url in self.recovery.get('gists', {}) or path in {r.get('path') for r in self.recovery.get('demos', [])}):
                reason = 'recorded retired or replaced runtime script'
            elif ref['tag'] in ('iframe', 'embed', 'object') and url in self.player_urls:
                reason = 'recorded player migration'
            elif parsed.path.rstrip('/').endswith('/trackback'):
                reason = 'retired trackback submission endpoint'
            elif ref['tag'] == 'link' and parsed.path.startswith('/wp-json/oembed/'):
                reason = 'retired WordPress oEmbed discovery endpoint'
            elif parsed.path.startswith('/wp-admin/'):
                reason = 'retired WordPress administration link'
            elif parsed.path.endswith('/function.file-exists'):
                reason = 'link inside a removed host diagnostic'
            elif url in self.failed_paths and any(v['url'].startswith('/unavailable/') for v in added):
                reason = 'captured unavailable URL'
            elif parsed.fragment == 'respond' and (ref['tag'], ref['attribute'], url.rsplit('#', 1)[0] + '#comments') in added_keys:
                reason = 'read-only comments anchor'
            elif parsed.fragment and any(tag == ref['tag'] and attr == ref['attribute'] and urlsplit(target).fragment == parsed.fragment and self.capture_aliases.get(urldefrag(target)[0]) == urldefrag(url)[0] for tag, attr, target in added_keys):
                reason = 'same-page anchor on a captured redirect alias'
            elif parsed.hostname in ('technorati.com', 'www.technorati.com') and parsed.path.startswith('/tag/'):
                slug = re.sub(r'[^\w.-]+', '-', normalize_space(unquote(parsed.path[5:].replace('+', ' '))).casefold()).strip('-.') or 'tag'
                if (ref['tag'], ref['attribute'], '/topics/' + slug + '/') in added_keys:
                    reason = 'local topic index for the same tag'
                elif not parsed.path[5:] and not ref['label']:
                    reason = 'empty legacy tag link'
            elif ref['tag'] == 'img' and any(canonical(k) == url and 'error' in v for k, v in self.images.items()):
                if any(v['tag'] == 'img' and v['url'] in ('/archive-assets/unavailable.svg', '/archive-assets/feed.svg') for v in added):
                    reason = 'recorded unavailable external image'
            if reason:
                explained.append({'reference': ref, 'reason': reason})
            else:
                problems.append(ref)
        return problems, explained

    def fragment_status(self, ref, original_refs):
        candidates = [v for v in original_refs if v['tag'] == ref['tag'] and v['label'] == ref['label'] and
                      (v['url'] == ref['url'] or v['url'].endswith('#respond') and v['url'][:-8] + '#comments' == ref['url'])]
        for old in candidates:
            url, fragment = urldefrag(old['url'])
            source = self.source_files.get(url)
            if source:
                return 'inherited' if fragment not in fragment_ids(source) else 'unexplained'
        return 'unverified'

    def text_pair(self, raw, clone):
        notes = []
        # Exact family of host diagnostics already removed during migration.
        warning = r'<b>(?:Warning|Notice|Deprecated)</b>\s*:[^\n]*?open_basedir[^\n]*?/home/[^\n]*?<br\s*/?>'
        raw, count = re.subn(warning, '', raw, flags=re.I)
        if count:
            notes.append('retired-host-open_basedir-warning')
        # Replace only an exact recorded source fragment, never an entire post.
        for group, records in [('code', self.recovery.get('code_blocks', [])),
                               ('literal-markup', self.ui.get('literal_markup', [])),
                               ('literal-comment', self.repairs.get('literal_fragments', []))]:
            for record in records:
                if record['captured'] in raw:
                    replacement = record.get('replacement', '<pre>' + html.escape(record.get('code', '')) + '</pre>')
                    raw = raw.replace(record['captured'], replacement)
                    notes.append(group + ': ' + str(record.get('id', record.get('post_id'))))
        for record in self.recovery.get('tag_lists', []):
            if record['captured'] in raw:
                raw = raw.replace(record['captured'], 'Technorati Tags: ' + ' , '.join(record['tags']))
                notes.append('tags: ' + str(record['post_id']))
        original = BeautifulSoup(raw, 'html.parser')
        actual = BeautifulSoup(clone, 'html.parser')
        for paragraph in original.select('.entry p'):
            for record in self.repairs.get('excerpts', []):
                if paragraph.get_text() == record['captured_text']:
                    paragraph.clear()
                    paragraph.string = record['text']
                    notes.append('excerpt: ' + str(record['post_id']))
        for record in self.ui.get('paragraph_code', []):
            for paragraph in original.find_all('p'):
                if normalize_space(paragraph.get_text(' ', strip=True)) == record['captured_text']:
                    paragraph.clear()
                    paragraph.string = record.get('prefix', '') + ' ' + record['code']
                    notes.append('paragraph-code: ' + record['id'])
        for src, record in self.recovery.get('gists', {}).items():
            for script in original.find_all('script', src=src):
                # Gist filenames/code are compared, not silently discarded.
                replacement = original.new_tag('div')
                replacement.string = ' '.join(f['code'] + ' ' + f['name'] + ' · Original gist' for f in record['files'])
                script.replace_with(replacement)
                notes.append('gist: ' + src)
        for record in self.recovery.get('comments', []):
            node = actual.find(id='comment-' + str(record['id']))
            if node and not original.find(id=node['id']):
                node.decompose()
                notes.append('recovered-comment: ' + str(record['id']))
                old_heading, new_heading = original.find(id='comments'), actual.find(id='comments')
                if not old_heading and new_heading and new_heading.get_text(' ', strip=True) == '1 Response':
                    new_heading.decompose()
        for node in original.select('textarea[name=ak_hp_textarea]'):
            label = node.parent
            if label.name == 'label' and label.get_text(strip=True) == 'Δ':
                label.decompose()
                notes.append('retired-spam-honeypot')
        for record in self.videos:
            if record.get('note'):
                for node in actual.select('.archive-video-note'):
                    if node.get_text(' ', strip=True) == record['note']:
                        node.decompose()
                        notes.append('player-note: ' + str(record['post_id']))
        audio = self.ui.get('audio', {})
        if audio.get('captured_label'):
            for node in original.find_all(string=audio['captured_label']):
                node.replace_with(audio['label'])
                notes.append('podcast-label')
        # Validate exact notice/footer text before treating it as expected.
        for node in actual.select('.archive-form-notice'):
            if node.get_text(' ', strip=True) == 'This form no longer accepts submissions.':
                node.decompose()
                notes.append('submission-notice')
        old_footer = original.select_one('#footer p')
        new_footer = actual.select_one('#footer p')
        if old_footer and new_footer:
            old = normalize_space(old_footer.get_text(' ', strip=True))
            new = normalize_space(new_footer.get_text(' ', strip=True))
            if old == 'Privacy Policy justaddwater.dk is proudly powered by WordPress' and new == 'Privacy Policy justaddwater.dk was proudly powered by WordPress . It is now a static site ( source ).':
                new_footer.clear()
                new_footer.string = old
                notes.append('archive-footer')
        # Player explanatory notes are retained in the raw diff; their presence
        # is never a reason to hide other differences in the containing article.
        return visible_text(original), visible_text(actual), sorted(set(notes))


def health(soup):
    result = []
    text = visible_text(soup)
    for code, pattern in [('shortcode', r'\[(?:/?code\b[^\]]*|/?tags)\]'),
                          ('php-warning', r'(?:Warning|Notice|Deprecated)\s*:\s*[^\n]{0,150}open_basedir')]:
        matches = re.findall(pattern, text, re.I)
        if matches:
            result.append((code, sorted(set(matches))))
    flash = [str(t.get('data') or t.get('src') or '') for t in soup.select('object, embed')
             if '.swf' in str(t).lower() or 'shockwave-flash' in str(t).lower()]
    if flash:
        result.append(('flash-player', flash))
    disabled = []
    for form in soup.select('.archive-form'):
        if form.select('input:not([disabled]), textarea:not([disabled]), button:not([disabled]), select:not([disabled])'):
            disabled.append(form.get('id', '(unnamed form)'))
    if disabled:
        result.append(('enabled-archived-form', disabled))
    ids = Counter(t['id'] for t in soup.select('[id]') if t['id'])
    if any(n > 1 for n in ids.values()):
        result.append(('duplicate-id', {k: n for k, n in ids.items() if n > 1}))
    return dict(result)


def refs(soup, base, prefix=''):
    result = []
    for tag in soup.select('[href], [src], [poster], object[data]'):
        for attr in ('href', 'src', 'poster', 'data'):
            value = tag.get(attr)
            if not value or value.startswith(('javascript:', 'mailto:', 'data:', 'tel:', 'about:')):
                continue
            if tag.name == 'link' and not set(tag.get('rel', [])) & {'stylesheet', 'icon', 'alternate'}:
                continue
            result.append({'tag': tag.name, 'attribute': attr, 'url': canonical(value, base, prefix),
                           'label': normalize_space(tag.get_text(' ', strip=True))[:160]})
    # srcset and CSS dependencies are included in the resource inventory.
    for tag in soup.select('[srcset]'):
        for candidate in tag['srcset'].split(','):
            parts = candidate.split()
            if parts and not parts[0].startswith('data:'):
                result.append({'tag': tag.name, 'attribute': 'srcset', 'url': canonical(parts[0], base, prefix), 'label': ''})
    css = '\n'.join(t.get('style', '') for t in soup.select('[style]')) + '\n' + '\n'.join(t.decode_contents() for t in soup.select('style'))
    for value in re.findall(r'url\([\s\'"]*([^\)\'"\s]+)', css):
        if not value.startswith('data:'):
            result.append({'tag': 'css', 'attribute': 'url', 'url': canonical(value, base, prefix), 'label': ''})
    return result


def snapshot(cache, url):
    stem = cache / digest(url)
    body = stem.with_suffix('.body')
    meta = read_json(stem.with_suffix('.json'), {})
    return body if body.is_file() else None, meta


def decode(body, content_type=''):
    match = re.search(r'charset=([^;\s]+)', content_type, re.I)
    encodings = [match[1].strip('"\'')] if match else []
    # Respect BOMs and HTML meta encodings, including old UTF-16 downloads.
    return UnicodeDammit(body, known_definite_encodings=encodings, is_html=True).unicode_markup or ''


def is_html(body, content_type, path):
    if Path(urlsplit(path).path).suffix.lower() in {'.js', '.css', '.json', '.xml', '.rss', '.atom', '.txt', '.rtf', '.pdf'}:
        return False
    return 'text/html' in content_type or path.endswith(('.html', '.htm')) or bool(re.search(br'<(?:!doctype\s+html|html)\b', body[:500], re.I))


def audit_record(path, url, kind, cache, site, policy, prefix, failure=None):
    source, meta = snapshot(cache, url)
    clone = local_file(site, path)
    row = {'id': digest(path)[:16], 'path': path, 'url': ORIGIN + path, 'capture_url': url, 'kind': kind,
           'source': str(source) if source else None, 'clone': str(clone) if clone else None,
           'captured_at': meta.get('captured_at'), 'source_status': meta.get('status'),
           'original_final_url': meta.get('final_url'), 'findings': []}
    issues = row['findings']
    if not source:
        issues.append(finding('baseline', 'unverified', 'Original capture failed.' if failure else 'Original response is absent from the cache.', error=failure))
        if clone:
            issues.append(finding('recovered-url', 'expected', 'This previously unavailable URL now has a local file.'))
        return row
    if not clone:
        issues.append(finding('missing-url', 'unexplained', 'Captured URL has no file at the same archive path.'))
        return row
    a, b = source.read_bytes(), clone.read_bytes()
    row.update(source_sha256=digest(a), clone_sha256=digest(b))
    content_type = meta.get('headers', {}).get('Content-Type', '')
    row['content_type'] = content_type
    row['html'] = is_html(a, content_type, path)
    if not row['html']:
        if a != b:
            is_feed = '<rss' in b[:500].decode('utf-8', 'ignore') or b'<feed ' in b[:500]
            if is_feed:
                try:
                    left, right = ET.fromstring(a), ET.fromstring(b)
                    ids = lambda t: [n.text for n in t.iter() if n.tag.rsplit('}', 1)[-1] in ('guid', 'id')]
                    if ids(left) != ids(right):
                        issues.append(finding('feed-items', 'unexplained', 'Feed item identifiers or ordering differ.', before=ids(left), after=ids(right)))
                    else:
                        issues.append(finding('feed-rewrite', 'expected', 'Feed regenerated with the same ordered item IDs; article markup and site URLs may differ.'))
                    def item_fields(tree):
                        return [{child.tag.rsplit('}', 1)[-1]: normalize_space(html.unescape(child.text or ''))
                                 for child in item if child.tag.rsplit('}', 1)[-1] in ('title', 'pubDate', 'published', 'updated')}
                                for item in tree.iter() if item.tag.rsplit('}', 1)[-1] in ('item', 'entry')]
                    if item_fields(left) != item_fields(right):
                        issues.append(finding('feed-fields', 'unexplained', 'Feed item titles or timestamps differ.', before=item_fields(left), after=item_fields(right)))
                except ET.ParseError as e:
                    issues.append(finding('feed-xml', 'unexplained', str(e)))
            elif path.endswith('.css'):
                # Retain the complete diff; CSS differences can affect every page.
                def css_key(text, base):
                    return re.sub(r'url\(\s*[\'"]?([^\)\'"\s]+)[\'"]?\s*\)', lambda m: 'url(' + canonical(m[1], base, prefix) + ')', text)
                na = css_key(a.decode('utf-8', 'replace'), url)
                nb = css_key(b.decode('utf-8', 'replace'), 'http://archive.test' + prefix + path)
                issues.append(finding('stylesheet', 'expected' if na == nb else 'unexplained', 'Stylesheet differs.', diff=list(difflib.unified_diff(na.splitlines(), nb.splitlines(), lineterm=''))))
            else:
                issues.append(finding('asset-bytes', 'unexplained', 'Downloaded asset bytes differ from the saved response.'))
        return row
    raw, actual = decode(a, content_type), b.decode('utf-8', 'replace')
    old_soup, new_soup = BeautifulSoup(raw, 'html5lib'), BeautifulSoup(actual, 'html5lib')
    row['title'] = new_soup.title.get_text(' ', strip=True) if new_soup.title else path
    row['text_before'], row['text_after'] = visible_text(old_soup), visible_text(new_soup)
    expected_raw = raw
    recovery = policy.repairs.get('html_sources', {}).get(path)
    if recovery and recovery.get('capture_sha256') == digest(a):
        restored = (policy.root / recovery['file']).read_bytes() if recovery.get('file') else a
        if not recovery.get('sha256') or digest(restored) == recovery['sha256']:
            expected_raw = restored.decode(recovery['encoding'])
    expected, observed, notes = policy.text_pair(expected_raw, actual)
    if expected_raw != raw:
        notes.append('recorded HTML encoding recovery')
    row['expected_changes'] = notes
    changes = text_changes(expected, observed)
    if changes:
        issues.append(finding('text', 'unexplained', 'Text differs after the narrowly recorded exceptions.', changes=changes))
    elif row['text_before'] != row['text_after']:
        issues.append(finding('text', 'expected', 'Text differences match recorded repairs.', rules=notes))
    old_health, new_health = health(old_soup), health(new_soup)
    for key in sorted(old_health.keys() | new_health.keys()):
        state = 'inherited' if key in old_health and old_health[key] == new_health.get(key) else 'fixed' if key not in new_health else 'unexplained'
        if key == 'duplicate-id' and new_health.get(key) and all(old_health.get(key, {}).get(name, 0) >= count for name, count in new_health[key].items()):
            state = 'inherited'
        issues.append(finding(key, state, key.replace('-', ' ').capitalize(), before=old_health.get(key), after=new_health.get(key)))
    old_refs = refs(old_soup, meta.get('final_url', url))
    new_refs = refs(new_soup, 'http://archive.test' + prefix + path, prefix)
    row['references'] = {'original': old_refs, 'clone': new_refs}
    switched = switched_links(old_refs, new_refs)
    if switched:
        issues.append(finding('link-label-target', 'unexplained', 'Link destinations are still present but attached to different labels.', links=switched))
    old_keys = {(v['tag'], v['attribute'], v['url']) for v in old_refs}
    new_keys = {(v['tag'], v['attribute'], v['url']) for v in new_refs}
    row['reference_changes'] = {'removed': [v for v in old_refs if (v['tag'], v['attribute'], v['url']) not in new_keys],
                                'added': [v for v in new_refs if (v['tag'], v['attribute'], v['url']) not in old_keys]}
    changed, explained = policy.reference_issues(row['reference_changes']['removed'], new_refs, path, raw)
    row['reference_changes']['explained'] = explained
    if changed:
        issues.append(finding('changed-reference', 'unexplained', 'Original links or dependencies were removed or changed without an exact recorded URL match.', references=changed))
    missing, fragments = [], []
    for ref in new_refs:
        u = urlsplit(ref['url'])
        if not u.netloc and u.path and not local_file(site, u.path):
            missing.append(ref)
        elif not u.netloc and u.fragment:
            target = local_file(site, u.path or path)
            if target and target.suffix.lower() in ('.html', '.htm') and u.fragment not in fragment_ids(target):
                fragments.append(ref)
    if missing:
        issues.append(finding('local-target', 'unexplained', 'Local link or resource has no target file.', references=missing))
    if fragments:
        for status in ('inherited', 'unexplained', 'unverified'):
            group = [ref for ref in fragments if policy.fragment_status(ref, old_refs) == status]
            if group:
                issues.append(finding('fragment-target', status, 'Local fragment links have no matching ID or named anchor.', references=group))
    for form in new_soup.find_all('form'):
        if form.get('method', 'get').lower() != 'get' or canonical(form.get('action', ''), 'http://archive.test' + prefix + path, prefix) != '/archive-search/':
            issues.append(finding('active-submission', 'unexplained', 'A form remains outside the approved local search route.', action=form.get('action'), method=form.get('method', 'get')))
    placeholders = [t.get('data-original-url') for t in new_soup.select('img[data-original-url]') if 'unavailable.svg' in t.get('src', '')]
    if placeholders:
        issues.append(finding('unavailable-image', 'inherited', 'Original images still unavailable; the archive shows placeholders.', urls=sorted(set(placeholders))))
    # Missing whole comments/articles are unambiguous regardless of prose repairs.
    for selector, label in [('.post[id]', 'article'), ('li[id^=comment-]', 'comment')]:
        before, after = {t['id'] for t in old_soup.select(selector)}, {t['id'] for t in new_soup.select(selector)}
        if before - after:
            issues.append(finding('missing-' + label, 'unexplained', 'Original IDs are absent.', ids=sorted(before - after)))
    row['structure'] = {side: {name: len(s.select(name)) for name in ['h1', 'h2', 'h3', 'img', 'iframe', 'object', 'form', 'pre', 'audio']} for side, s in [('original', old_soup), ('clone', new_soup)]}
    inline_before = {normalize_space(t.decode_contents()): t.decode_contents() for t in old_soup.select('script:not([src])') if t.decode_contents().strip()}
    inline_after = {normalize_space(t.decode_contents()): t.decode_contents() for t in new_soup.select('script:not([src])') if t.decode_contents().strip()}
    changed_scripts = [inline_before[key] for key in inline_before.keys() - inline_after.keys()]
    handlers = [{'tag': t.name, 'attribute': name, 'code': value} for t in old_soup.find_all(True) for name, value in t.attrs.items() if name.lower().startswith('on')]
    row['inline_code'] = {'removed_scripts': changed_scripts, 'original_event_handlers': handlers}
    unknown_scripts = inline_review(changed_scripts)
    explained_inline = []
    for code in list(unknown_scripts):
        if any(code in record['captured'] and record['captured'] in raw for record in policy.recovery.get('code_blocks', [])):
            unknown_scripts.remove(code)
            explained_inline.append('Script is displayed as a recorded literal code example.')
        elif path == '/wp-content/uploads/2006/03/fixed-table-cells-notworking.html' and new_soup.select_one('script[src$="/archive-assets/demos.js"]'):
            unknown_scripts.remove(code)
            explained_inline.append('Table-height behavior is provided by the tested local demo script.')
    pending_handlers = []
    for handler in handlers:
        code = handler['code'].strip()
        if handler['tag'] == 'a' and (re.fullmatch(r'doPopup\(\d*\);return false;?', code) or code in ('return top.js.OpenExtLink(window,event,this)', 'return false;')):
            explained_inline.append('Obsolete link interception removed; the original destination remains a normal link.')
        elif handler == {'tag': 'input', 'attribute': 'onclick', 'code': "this.value=''"} and new_soup.select_one('.archive-form input[disabled]'):
            explained_inline.append('Clear-on-click handler belongs to the disabled historical submission form.')
        else:
            pending_handlers.append(handler)
    if explained_inline:
        issues.append(finding('inline-behavior', 'expected', 'Reviewed local behavior or inert examples.', reasons=sorted(set(explained_inline))))
    if unknown_scripts or pending_handlers:
        issues.append(finding('inline-behavior', 'review', 'Inline behavior changed. Check whether it was a demo, code example or retired widget.', scripts=unknown_scripts, handlers=pending_handlers))
    return row


def resources(root, cache, site, prefix):
    """Replay only saved responses, never substitute a repaired clone for HTML/CSS."""
    result = {}
    for meta_path in cache.glob('*.json'):
        if not re.fullmatch(r'[a-f0-9]{64}', meta_path.stem):
            continue
        body = meta_path.with_suffix('.body')
        if not body.is_file():
            continue
        meta = read_json(meta_path, {})
        if not meta.get('url'):
            continue
        item = {'file': str(body), 'contentType': meta.get('headers', {}).get('Content-Type', mimetypes.guess_type(meta['url'])[0] or 'application/octet-stream'),
                'status': meta.get('status', 200), 'provenance': 'capture'}
        for url in {meta['url'], meta.get('final_url', meta['url'])}:
            result[urldefrag(url)[0]] = item
    # External images were saved separately. Record their provenance explicitly;
    # these are reconstructed dependencies, not original response snapshots.
    for url, record in read_json(root / 'data/external-images.json', {}).items():
        file = local_file(site, record.get('path', '/__absent__'))
        if file and record.get('sha256') == digest(file.read_bytes()):
            result.setdefault(urldefrag(url)[0], {'file': str(file), 'contentType': mimetypes.guess_type(str(file))[0] or 'image/jpeg', 'status': 200, 'provenance': 'recovered-image'})
    clone = {}
    for file in site.rglob('*'):
        if not file.is_file():
            continue
        route = '/' + file.relative_to(site).as_posix()
        content_type = ('text/html; charset=utf-8' if file.suffix.lower() in ('.html', '.htm') else
                        'application/rss+xml' if file.name == 'index.xml' else mimetypes.guess_type(str(file))[0])
        item = {'file': str(file), 'contentType': content_type or 'application/octet-stream', 'status': 200, 'provenance': 'clone'}
        clone[prefix + route] = item
        if file.name in ('index.html', 'index.xml'):
            clone[prefix + route[:-len(file.name)]] = item
    # A set of redirect aliases has process-dependent iteration order. Stable
    # ordering prevents identical resources invalidating the browser cache.
    return {'original': dict(sorted(result.items())), 'clone': dict(sorted(clone.items()))}


def refresh_one(row, out, timeout):
    url = row['url']
    if urlsplit(url).hostname not in HOSTS:
        return {'error': 'Refresh is limited to the original site hosts.'}
    try:
        with urlopen(Request(url, headers={'User-Agent': 'JustAddWater archive comparison/1.0'}), timeout=timeout) as response:
            body = response.read(45 * 1024 * 1024 + 1)
            if len(body) > 45 * 1024 * 1024:
                raise ValueError('Response exceeds the 45 MiB capture limit')
            stem = out / digest(url)
            stem.with_suffix('.body').write_bytes(body)
            meta = {'url': url, 'final_url': response.url, 'status': response.status,
                    'headers': dict(response.headers), 'captured_at': datetime.now(timezone.utc).isoformat()}
            write_json(stem.with_suffix('.json'), meta)
            return {'status': response.status, 'changed_since_capture': digest(body) != row.get('source_sha256'), 'sha256': digest(body), 'final_url': response.url}
    except Exception as e:
        return {'error': str(e)}


def screenshot_coverage(info, width, height):
    expected = (info.get('viewport', {}).get('width', 1280), min(50000, info['height']))
    return None if (width, height) == expected else {'expected': list(expected), 'actual': [width, height]}


def visual_comparison(row, out):
    from PIL import Image, ImageChops, ImageEnhance
    sides = row.get('browser', {})
    if not all(sides.get(s, {}).get('screenshot') for s in ('original', 'clone')):
        return
    images = [Image.open(out / sides[s]['screenshot']).convert('RGB') for s in ('original', 'clone')]
    for side, im in zip(('original', 'clone'), images):
        mismatch = screenshot_coverage(sides[side], im.width, im.height)
        if mismatch:
            row['findings'].append(finding('screenshot-coverage', 'unexplained',
                'Screenshot dimensions do not cover the measured page up to the documented cap.', side=side, **mismatch))
    # Fixed scale preserves height/layout differences. This is a review signal,
    # not an assertion of correctness; JPEG noise below 45/255 is ignored.
    scale = 480 / max(im.width for im in images)
    resized = [im.resize((round(im.width * scale), round(im.height * scale))) for im in images]
    size = (max(im.width for im in resized), max(im.height for im in resized))
    canvases = []
    for im in resized:
        canvas = Image.new('RGB', size, 'white')
        canvas.paste(im, (0, 0))
        canvases.append(canvas)
    delta = ImageChops.difference(*canvases)
    mask = delta.convert('L').point(lambda p: 255 if p > 45 else 0)
    ratio = sum(mask.histogram()[1:]) / (size[0] * size[1])
    image = Image.blend(canvases[1], Image.new('RGB', size, 'white'), .7)
    image.paste(Image.new('RGB', size, '#dc2626'), mask=mask)
    name = 'screenshots/' + row['id'] + '-diff.png'
    image.save(out / name, optimize=True)
    row['visual'] = {'changed_pixel_fraction': round(ratio, 5), 'diff': name, 'scale': scale,
                     'original_height': sides['original']['height'], 'clone_height': sides['clone']['height']}
    for im in images:
        im.close()
    if ratio > .01:
        row['findings'].append(finding('visual', 'review', 'Rendered pages differ; inspect screenshots. Expected repairs also affect this score.', **row['visual']))


def merge_browser(rows, out):
    for row in rows:
        if not row.get('html'):
            continue
        data = read_json(out / 'browser' / (row['id'] + '.json'))
        if not data:
            continue
        if any(data.get(k) != row.get(k) for k in ('source_sha256', 'clone_sha256')):
            row['findings'].append(finding('browser-stale', 'unverified', 'Saved browser evidence predates the compared HTML; run --browser again.'))
            continue
        row['browser'] = data
        for side in ('original', 'clone'):
            info = data.get(side, {})
            if info.get('error'):
                row['findings'].append(finding('browser-capture', 'unverified', 'Browser capture failed.', side=side, error=info['error']))
            if info.get('truncated'):
                row['findings'].append(finding('screenshot-limit', 'unverified', 'Screenshot covers at most 1280 × 50000 pixels; overflow outside that rectangle is not visually compared.', side=side))
        for key in ('brokenImages', 'jsErrors', 'overflow', 'enabledArchivedControls'):
            a, b = data.get('original', {}).get(key, []), data.get('clone', {}).get(key, [])
            if a or b:
                status = 'inherited' if a == b else 'fixed' if not b else 'unexplained' if key == 'enabledArchivedControls' else 'review'
                if a and not b and key in ('brokenImages', 'jsErrors') and data.get('original', {}).get('blocked'):
                    status = 'unverified'
                row['findings'].append(finding('browser-' + key, status, 'Browser health: ' + key, before=a, after=b))
        old_width = data.get('original', {}).get('width', 0)
        new_width = data.get('clone', {}).get('width', 0)
        viewport_width = data.get('clone', {}).get('viewport', {}).get('width', 1280)
        if new_width > viewport_width:
            row['findings'].append(finding('page-overflow', 'inherited' if old_width == new_width else 'review',
                                          'Page content extends beyond the viewport.', before=old_width, after=new_width, viewport=viewport_width))
        styles = []
        old_geometry = data.get('original', {}).get('geometry', {})
        new_geometry = data.get('clone', {}).get('geometry', {})
        for selector in old_geometry.keys() & new_geometry.keys():
            for prop in ('background', 'color', 'font', 'textAlign'):
                a, b = old_geometry[selector].get(prop), new_geometry[selector].get(prop)
                if a != b:
                    styles.append({'selector': selector, 'property': prop, 'before': a, 'after': b})
        if styles:
            row['findings'].append(finding('computed-style', 'review', 'Computed theme styles differ, including color changes below the pixel-diff tolerance.', changes=styles))
        visual_comparison(row, out)


def render_report(rows, out, metadata):
    statuses = Counter(f['status'] for r in rows for f in r['findings'])
    kinds = Counter(f['kind'] for r in rows for f in r['findings'])
    metadata['counts'] = {'urls': len(rows), 'html_pairs': sum(r.get('html', False) for r in rows),
                          'browser_pairs': sum(all(r.get('browser', {}).get(s, {}).get('screenshot') for s in ('original', 'clone')) for r in rows),
                          'statuses': dict(statuses), 'kinds': dict(kinds)}
    groups = Counter((f['kind'], f['status']) for r in rows for f in r['findings'])
    metadata['finding_groups'] = [{'kind': key[0], 'status': key[1], 'count': count} for key, count in groups.most_common()]
    for row in rows:
        for f in row['findings']:
            f['id'] = digest(row['path'] + '\n' + json.dumps(f, sort_keys=True))[:16]
    write_json(out / 'report.json', {'metadata': metadata, 'urls': rows})
    details = out / 'pages'
    details.mkdir(exist_ok=True)
    esc = html.escape
    cards = []
    for row in rows:
        state = sorted({f['status'] for f in row['findings']}) or ['unchanged']
        body = '<p><a href="../index.html">← All URLs</a></p><h1>' + esc(row.get('title', row['path'])) + '</h1><p>' + esc(row['path']) + '</p>'
        body += '<p><a href="' + esc(row['url'], quote=True) + '">Original live URL</a> · <a href="https://watson.github.io/justaddwater.dk' + esc(row['path'], quote=True) + '">Published clone</a></p>'
        body += '<h2>Findings</h2>'
        for f in row['findings']:
            body += '<details><summary><b class="' + f['status'] + '">' + esc(f['status']) + '</b> · ' + esc(f['kind']) + ': ' + esc(f['message']) + '</summary><pre>' + esc(json.dumps(f, ensure_ascii=False, indent=2)) + '</pre></details>'
        if row.get('browser'):
            body += '<h2>Rendered comparison</h2><p>Offline replay at the same viewport. External players are blocked. Red marks pixels differing above the tolerance; scroll each image or open it at full size.</p><div class="screens">'
            for side in ('original', 'clone'):
                info = row['browser'].get(side, {})
                if info.get('screenshot'):
                    src = '../' + info['screenshot']
                    body += '<section><h3>' + side.capitalize() + '</h3><a href="' + src + '">Full image</a><div class="shot"><img loading="lazy" src="' + src + '"></div></section>'
            if row.get('visual'):
                body += '<section><h3>Pixel difference</h3><div class="shot"><img loading="lazy" src="../' + row['visual']['diff'] + '"></div></section>'
            body += '</div><details><summary>Browser evidence and unavailable replay dependencies</summary><pre>' + esc(json.dumps(row['browser'], ensure_ascii=False, indent=2)) + '</pre></details>'
        if row.get('text_before') != row.get('text_after'):
            body += '<h2>Raw text difference</h2><p>Includes expected changes; nothing is suppressed in this view.</p><pre class="diff">' + esc('\n'.join(difflib.unified_diff(textwrap.wrap(row.get('text_before', ''), 100), textwrap.wrap(row.get('text_after', ''), 100), fromfile='original', tofile='clone', lineterm=''))) + '</pre>'
        for key in ('expected_changes', 'reference_changes', 'structure', 'inline_code', 'live'):
            if row.get(key):
                body += '<details><summary>' + esc(key.replace('_', ' ').capitalize()) + '</summary><pre>' + esc(json.dumps(row[key], ensure_ascii=False, indent=2)) + '</pre></details>'
        (details / (row['id'] + '.html')).write_text(document(row['path'], body))
        rank = 0 if 'unexplained' in state else 1 if 'review' in state else 2 if 'inherited' in state else 3
        search = ' '.join(f['kind'] for f in row['findings'])
        group_keys = ' '.join(f['kind'] + ':' + f['status'] for f in row['findings'])
        cards.append((rank, row['path'], '<tr data-groups="' + esc(group_keys, quote=True) + '" data-state="' + ' '.join(state) + '" data-search="' + esc(search, quote=True) + '"><td><a href="pages/' + row['id'] + '.html">' + esc(row['path']) + '</a></td><td>' + esc(', '.join(state)) + '</td><td>' + str(len(row['findings'])) + '</td></tr>'))
    body = '<h1>Archive comparison</h1><p>' + esc(metadata['created_at']) + '</p><div class="stats">'
    for name, value in [('Inventoried URLs', len(rows)), ('HTML pairs', metadata['counts']['html_pairs']), ('Browser pairs', metadata['counts']['browser_pairs']), ('Unexplained findings', statuses['unexplained'])]:
        body += '<div><strong>' + str(value) + '</strong><span>' + name + '</span></div>'
    body += '</div><p>Compare the original capture with the static archive. <b>Unexplained</b> means investigate; it does not prove a regression. <b>Review</b> includes visual differences and browser signals. <b>Inherited</b> issues occur on both sides or were already recorded as unavailable. <b>Unverified</b> identifies missing evidence.</p><p>Offline browser replay uses saved responses and separately recovered external images. Missing dependencies and third-party players are blocked and listed, not treated as proof of live failures. Form controls are inspected without submitting anything. Text differences retain a raw view alongside the scoped expected repairs.</p>'
    body += '<details><summary>Coverage, configuration and limitations</summary><pre>' + esc(json.dumps(metadata, ensure_ascii=False, indent=2)) + '</pre></details><p><a href="report.json">Download complete JSON</a></p><label>Find a URL or issue <input id="query" type="search" placeholder="URL, issue type or status"></label> <label>Status <select id="status"><option value="">All</option>'
    for s in ('unexplained', 'review', 'inherited', 'fixed', 'expected', 'unverified', 'unchanged'):
        body += '<option>' + s + '</option>'
    body += '</select></label><details><summary>Group issues by category</summary><p>'
    for (kind, status), count in groups.most_common():
        if status in ('unexplained', 'review', 'inherited'):
            body += '<button type="button" data-kind="' + esc(kind, quote=True) + '" data-status="' + status + '">' + esc(kind) + ' · ' + status + ' (' + str(count) + ')</button> '
    body += '</p></details><p id="count"></p><table><thead><tr><th>URL</th><th>Status</th><th>Findings</th></tr></thead><tbody>' + ''.join(c[2] for c in sorted(cards)) + '</tbody></table><script>const q=document.querySelector("#query"),s=document.querySelector("#status"),rows=[...document.querySelectorAll("tbody tr")];function filter(group=""){let n=0;for(const r of rows){r.hidden=!!group&&!r.dataset.groups.split(" ").includes(group)||!((r.textContent+" "+r.dataset.search).toLowerCase().includes(q.value.toLowerCase())&&(!s.value||r.dataset.state.split(" ").includes(s.value)));if(!r.hidden)n++}document.querySelector("#count").textContent=n+" URLs shown"}q.addEventListener("input",()=>filter());s.addEventListener("change",()=>filter());document.querySelectorAll("button[data-kind]").forEach(b=>b.addEventListener("click",()=>{q.value=b.dataset.kind;s.value=b.dataset.status;filter(b.dataset.kind+":"+b.dataset.status)}));filter();</script>'
    (out / 'index.html').write_text(document('Archive comparison', body))
    return metadata['counts']


def document(title, body):
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>' + html.escape(title) + '</title><style>body{font:16px/1.5 system-ui,sans-serif;color:#1e293b;background:#f8fafc;max-width:1400px;margin:32px auto;padding:0 24px}h1{font-size:32px}a{color:#0369a1}table{border-collapse:collapse;width:100%;background:white}td,th{text-align:left;border-bottom:1px solid #e2e8f0;padding:10px;overflow-wrap:anywhere}td:first-child{width:68%}details{border:1px solid #cbd5e1;padding:12px;margin:12px 0;background:white}summary{cursor:pointer}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px;max-height:650px;overflow:auto}.stats{display:flex;gap:16px;flex-wrap:wrap}.stats div{background:white;border:1px solid #cbd5e1;padding:16px 24px}.stats strong{display:block;font-size:28px}.stats span{font-size:14px}.unexplained{color:#b91c1c}.inherited,.review{color:#92400e}.fixed{color:#166534}.screens{display:flex;gap:16px}.screens section{min-width:0;flex:1}.shot{max-height:700px;overflow:auto;border:1px solid #cbd5e1}.shot img{width:100%;display:block}input,select{font:inherit;padding:8px;border:1px solid #94a3b8;border-radius:4px}input{width:320px}tr[hidden]{display:none}@media(max-width:700px){.screens{display:block}input{width:80%}}</style><body>' + body + '</body></html>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=ROOT / '.cache')
    parser.add_argument('--site', type=Path, default=ROOT / 'site')
    parser.add_argument('--output', type=Path, default=ROOT / '.cache/audit')
    parser.add_argument('--base-path', default='')
    parser.add_argument('--match', default='', help='Only paths containing this string')
    parser.add_argument('--limit', type=int)
    parser.add_argument('--browser', action='store_true', help='Render every selected HTML pair offline')
    parser.add_argument('--browser-workers', type=int, default=3)
    parser.add_argument('--browser-executable', help='Optional system Chromium/Chrome path')
    parser.add_argument('--refresh', action='store_true', help='GET originals into a separate live snapshot; never overwrite the capture')
    parser.add_argument('--fail-on-unexplained', action='store_true')
    parser.add_argument('--report-only', action='store_true', help='Rebuild report from existing static/browser evidence')
    args = parser.parse_args()
    args.base_path = '/' + args.base_path.strip('/') if args.base_path.strip('/') else ''
    args.site, args.cache, args.output = args.site.resolve(), args.cache.resolve(), args.output.resolve()
    if args.output.is_relative_to(args.site):
        parser.error('Reports must be outside the published site directory')
    args.output.mkdir(parents=True, exist_ok=True)
    if args.report_only:
        stored = read_json(args.output / 'static.json')
        if not stored:
            parser.error('No static.json in the output directory')
        rows, metadata = stored['urls'], stored['metadata']
        args.site, args.cache = Path(metadata['site']), Path(metadata['cache'])
        args.base_path = metadata['base_path']
    else:
        inventory = read_json(args.cache / 'capture.json')
        if not inventory:
            parser.error('Capture inventory is missing; run scripts/archive.py capture or supply --cache')
        inventory['pages'] = inventory.get('pages', {}) | read_json(ROOT / 'data/supplemental-capture.json', {}).get('pages', {})
        policy = Expectations(ROOT, args.cache)
        jobs = {}
        for kind in ('pages', 'assets', 'failed_pages', 'failed_assets'):
            for path, value in inventory.get(kind, {}).items():
                jobs.setdefault(path, (path, ORIGIN + path if kind.startswith('failed') else value, kind,
                                        value if kind.startswith('failed') else None))
        selected = [j for p, j in sorted(jobs.items()) if args.match in p]
        if args.limit is not None:
            selected = selected[:args.limit]
        rows = []
        for i, (path, url, kind, failure) in enumerate(selected, 1):
            rows.append(audit_record(path, url, kind, args.cache, args.site, policy, args.base_path, failure))
            if i % 100 == 0:
                print(f'Static comparison: {i}/{len(selected)}', flush=True)
        compared = {Path(r['clone']) for r in rows if r.get('clone')}
        metadata = {'created_at': datetime.now(timezone.utc).isoformat(), 'policy_version': POLICY_VERSION,
                    'site': str(args.site), 'cache': str(args.cache), 'base_path': args.base_path,
                    'inventory_urls': len(jobs), 'selected_urls': len(rows), 'selection': {'match': args.match, 'limit': args.limit},
                    'generated_html_without_capture': ['/' + p.relative_to(args.site).as_posix() for p in sorted(args.site.rglob('*.html')) if p not in compared],
                    'limitations': ['Browser replay cannot verify third-party video availability or uncaptured remote scripts.',
                                    'Recovered external images reconstruct baseline dependencies; they are labeled in browser evidence.',
                                    'Pixel differences include intentional changes and are review signals, not automatic failures.',
                                    'Controls are inspected, not clicked; demo behavior still needs interaction tests.',
                                    'Generated clone-only pages are inventoried separately; existing verify.py validates their local links.',
                                    'DOM checks use HTML5 parsing; text expectations use an independent literal-fragment comparison.',
                                    'Live refresh detects drift and saves separate responses; it does not replace the baseline comparison.']}
        if args.refresh:
            live = args.output / 'live'
            live.mkdir(exist_ok=True)
            with ThreadPoolExecutor(max_workers=2) as pool:
                for row, result in zip(rows, pool.map(lambda r: refresh_one(r, live, 25), rows)):
                    row['live'] = result
        write_json(args.output / 'static.json', {'metadata': metadata, 'urls': rows})
    if args.browser:
        manifest = {'rows': [{**{k: r[k] for k in ('id', 'path', 'source', 'clone', 'source_sha256', 'clone_sha256')}, 'url': r.get('original_final_url') or r['url']} for r in rows if r.get('html')],
                    'resources': resources(ROOT, args.cache, args.site, args.base_path), 'output': str(args.output),
                    'basePath': args.base_path, 'workers': args.browser_workers, 'executablePath': args.browser_executable}
        write_json(args.output / 'manifest.json', manifest)
        subprocess.run(['node', str(ROOT / 'scripts/audit_browser.mjs'), str(args.output / 'manifest.json')], check=True)
    merge_browser(rows, args.output)
    counts = render_report(rows, args.output, metadata)
    print(json.dumps(counts, indent=2))
    print('Report: ' + str(args.output / 'index.html'))
    return 1 if args.fail_on_unexplained and counts['statuses'].get('unexplained') else 0


if __name__ == '__main__':
    sys.exit(main())
