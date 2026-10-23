#!/usr/bin/env python3
"""Build a public migration ledger from reviewed manifests, never private backups.

Counts describe source references and documented changes, not distinct defects.
The page/resource index follows deployed HTML and CSS; it does not probe the web.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit

from resources import css_urls

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
REPORT_PATH = '/migration-report/'
REPO = 'https://github.com/watson/justaddwater.dk/blob/main/'
INPUTS = ('content', 'recovery', 'ui-repairs', 'external-images', 'external-resources',
          'video-players', 'audit-repairs', 'audit-repair-report', 'audit-summary',
          'audit-new-findings', 'code-block-review', 'comment-restoration-report',
          'supplemental-capture', 'feed-aliases', 'missing-image-rendering')
CATEGORIES = {'recovered': 'Recovered content', 'repaired': 'Rendering & behavior',
              'preserved': 'Kept locally'}


def plain(value):
    return html.unescape(re.sub('<[^>]+>', '', value)).strip()


def route(file):
    value = '/' + file.relative_to(SITE).as_posix()
    return value[:-10] if value.endswith('index.html') else value


def normalized(value, base='/'):
    url = urlsplit(urljoin('http://justaddwater.dk' + base, html.unescape(value)))
    if url.scheme in ('http', 'https') and url.hostname in ('justaddwater.dk', 'www.justaddwater.dk'):
        return unquote(url.path)
    return value


class Page(HTMLParser):
    def __init__(self, path, source):
        super().__init__(convert_charrefs=True)
        self.path, self.source = path, source
        self.refs, self.codes, self.ids, self.classes = set(), set(), set(), set()
        self.title, self.in_title, self.in_style = '', False, False
        self.feed_links, self.players = [], []
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        self.in_title = self.in_title or tag == 'title'
        self.in_style = self.in_style or tag == 'style'
        self.classes.update((a.get('class') or '').split())
        if a.get('id'):
            self.ids.add(a['id'])
        if a.get('data-recovery-code'):
            self.codes.add(a['data-recovery-code'])
        for key in ('src', 'href', 'poster', 'data', 'background'):
            if a.get(key):
                self.refs.add(normalized(a[key], self.path))
        for url in css_urls(a.get('style', '')):
            self.refs.add(normalized(url, self.path))
        for value in (a.get('srcset') or '').split(','):
            if value.strip():
                self.refs.add(normalized(value.split()[0], self.path))
        if tag == 'iframe' and 'youtube.com/embed/' in a.get('src', ''):
            self.players.append(a)

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'style':
            self.in_style = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_style:
            self.refs.update(normalized(u, self.path) for u in css_urls(data))


def dependency_closure(start, graph):
    result, pending = set(), list(start)
    while pending:
        path = pending.pop()
        if path in result:
            continue
        result.add(path)
        pending.extend(graph.get(path, ()))
    return result


def image_outcome(record):
    if not record.get('path'):
        return 'Not recovered'
    if 'web.archive.org/' in record.get('fetched_from', ''):
        return 'Recovered from Internet Archive'
    if record.get('recovered_from'):
        return 'Recovered from site files'
    if record.get('note') and 'mistakenly' in record['note']:
        return 'Repaired source URL'
    return 'Saved from publisher or image host'


def original_source(url):
    match = re.match(r'https?://web\.archive\.org/web/[^/]+/(https?://.*)', url)
    return match[1] if match else url


def build_report():
    data = {name: json.loads((ROOT / f'data/{name}.json').read_text()) for name in INPUTS}
    content, recovery, ui, audit = (data[n] for n in ('content', 'recovery', 'ui-repairs', 'audit-repairs'))
    articles = {row['id']: {'path': normalized(row['link']), 'title': plain(row['title']['rendered'])}
                for row in content['posts'] + content['pages']}
    titles = {r['path']: r['title'] for r in articles.values()}
    pages = {}
    for file in sorted(SITE.rglob('*.html')):
        path = route(file)
        if path.startswith(REPORT_PATH) or path.startswith('/archive-assets/') and path != '/archive-assets/demos/undo.html':
            continue
        pages[path] = Page(path, file.read_text())
    graph = {}
    for file in sorted(SITE.rglob('*.css')):
        path = '/' + file.relative_to(SITE).as_posix()
        if path.endswith('/migration-report.css'):
            continue
        graph[path] = {normalized(u, path) for u in css_urls(file.read_text())}
    # Only resource edges are followed: an ordinary link to another article
    # must not make all of that article's resources belong to the linking page.
    resource_users = defaultdict(set)
    for path, page in pages.items():
        for ref in dependency_closure(page.refs, graph):
            resource_users[ref].add(path)

    def family(path):
        return re.sub(r'comment-page-\d+/$', '', path)

    def primary(path):
        return path in titles or path.startswith('/wp-content/') or path == '/archive-assets/demos/undo.html'

    def describe_page(path):
        return {'path': path, 'title': titles.get(path) or plain(pages[path].title).removeprefix('justaddwater.dk | ').strip() or unquote(path.rsplit('/', 1)[-1]) or 'Homepage',
                'original_url': 'http://humanized.com/weblog/images/resources/undo/todo.html' if path == '/archive-assets/demos/undo.html' else 'http://justaddwater.dk' + path,
                'kind': 'Article or page' if path in titles else 'Demo or download' if primary(path) else 'Archive or alternate page'}

    resources, changes = [], []

    def add_resource(source, path, kind, outcome, evidence, retrieved='', note='', owners=(), digest=''):
        local = SITE / unquote(path.lstrip('/')).split('#')[0]
        if not local.is_file() and not (kind.startswith('Inline gist:') and (local / 'index.html').is_file()):
            raise ValueError('Recorded preserved resource is absent: ' + path)
        used = sorted(set(owners) if kind.startswith('Inline gist:') else resource_users.get(unquote(path.split('#')[0]), set()) | set(owners))
        record = {'id': 'resource-' + hashlib.sha256(source.encode()).hexdigest()[:12],
                  'source': source, 'path': path, 'kind': kind, 'outcome': outcome,
                  'retrieved_from': retrieved, 'note': note, 'evidence': evidence,
                  'sha256': digest, 'pages': used}
        resources.append(record)
        return record

    def copies(paths):
        selected = set(paths)
        return sorted(p for p in pages if p in selected or family(p) in selected)

    def add_change(key, title, categories, outcome, before, after, paths=(), evidence=(), asset_ids=(), sitewide=False):
        paths = copies(paths)
        changes.append({'id': key, 'title': title, 'categories': categories, 'outcome': outcome,
                        'before': before, 'after': after, 'pages': paths, 'evidence': list(evidence),
                        'resources': list(asset_ids), 'sitewide': sitewide})

    for source, r in sorted(data['external-images'].items()):
        if r.get('path'):
            add_resource(source, r['path'], 'Image', image_outcome(r), 'data/external-images.json',
                         r.get('fetched_from', ''), r.get('note', r.get('recovered_from', 'Google menus screenshot.' if '/google/gmenu_' in source else '')), digest=r['sha256'])
    for source, r in sorted(data['external-resources']['resources'].items()):
        if r.get('path'):
            add_resource(source, r['path'], 'Stylesheet' if r['kind'] == 'stylesheet' else 'CSS image',
                         'Recovered from Internet Archive' if 'web.archive.org/' in r['fetched_from'] else 'Saved from publisher',
                         'data/external-resources.json', r['fetched_from'], ' '.join(r.get('adaptations', [])), digest=r['sha256'])
    for r in recovery['assets']:
        add_resource('http://justaddwater.dk' + r['path'], r['path'], 'Image', 'Recovered from site backup',
                     'data/recovery.json', note='Original upload recovered from the old WordPress files.', digest=r['sha256'])
    for r in ui['bookmarklet_assets']:
        # Bookmarklets load scripts dynamically. Associate their shared bundle
        # explicitly with the reviewed toolbox pages, rather than guessing JS.
        owners = [p for p in ui['bookmarklets'] if ('cookieeditor' in p) == ('cookieeditor' in r['path'])]
        retrieved = r['source_url'] if urlsplit(r['source_url']).scheme in ('http', 'https') else ''
        backup_sources = {'/archive-assets/bookmarklets/cookieeditor.js': 'http://justaddwater.dk/wp-content/uploads/2007/01/cookieeditor.js'}
        source = original_source(retrieved) if retrieved else backup_sources[r['path']]
        note = 'Shared reviewed toolbox bundle; may load only when a tool is invoked.' if retrieved else r['source_url']
        add_resource(source, r['path'], 'Bookmarklet dependency', 'Recovered and adapted locally',
                     'data/ui-repairs.json', retrieved, note, owners, r['sha256'])
    audio = ui['audio']
    add_resource(audio['source_url'], audio['path'], 'Audio', 'Recovered from publisher', 'data/ui-repairs.json',
                 audio['source_url'], audio['note'], [articles[audio['post_id']]['path'], *audio['transcripts']], audio['sha256'])
    for source, gist in recovery['gists'].items():
        for index, file in enumerate(gist['files'], 1):
            # The content is inline; the link opens the article (recorded
            # anchors are data attributes, not HTML fragment destinations).
            owners = [p for p, page in pages.items() if f'gist-{gist["post_id"]}-{index}' in page.codes]
            add_resource(file['source_url'], gist['article'], 'Inline gist: ' + file['name'], 'Saved at recorded revision',
                         'data/recovery.json', file['source_url'], 'Gist revision ' + gist['revision'], owners, file['sha256'])
    undo = next(r for r in recovery['demos'] if r.get('local_path'))
    add_resource(undo['source_url'], undo['local_path'], 'Embedded demo', 'Recovered and adapted locally',
                 'data/recovery.json', undo['archived_source'], undo['status'], [undo['article'], undo['local_path']])
    for path, r in audit['html_sources'].items():
        if r.get('file'):
            add_resource('http://justaddwater.dk' + path, path, 'HTML download', 'Recovered from site backup',
                         'data/audit-repairs.json', note=r['evidence'], owners=[path], digest=r['sha256'])

    # Image changes are grouped by recovery method, with every resource and
    # affected HTML copy retained in the downloadable inventory.
    for outcome in sorted({r['outcome'] for r in resources if r['kind'] == 'Image'}):
        rows = [r for r in resources if r['kind'] == 'Image' and r['outcome'] == outcome]
        recovered = outcome.startswith('Recovered') or outcome.startswith('Repaired')
        add_change('images-' + hashlib.sha256(outcome.encode()).hexdigest()[:8], outcome,
                   ['recovered', 'preserved'] if recovered else ['preserved'], outcome,
                   'Images depended on old upload paths or external hosts. Archive/backup recoveries and corrected image URLs are distinguished from successful direct captures.',
                   f'{len(rows)} source references now resolve to local image files. Different URLs can share the same recovered bytes.',
                   {p for r in rows for p in r['pages']}, ['data/external-images.json', 'data/recovery.json'], [r['id'] for r in rows])
    styles = [r for r in resources if r['kind'] in ('Stylesheet', 'CSS image')]
    add_change('external-styles', 'Capgemini map styling and CastingWords transcripts', ['recovered', 'repaired', 'preserved'], 'Restored styles with recorded omissions',
               'The map examples and podcast transcripts depended on external stylesheets and their background images.',
               'Five stylesheets and 21 decorative images are local. Missing unused backgrounds and obsolete IE5 imports were removed; a missing navigation sprite falls back to its existing text label. This does not recreate every historical decoration.',
               {p for r in styles for p in r['pages']}, ['data/external-resources.json'], [r['id'] for r in styles])
    for path, r in audit['html_sources'].items():
        add_change('encoding-' + hashlib.sha256(path.encode()).hexdigest()[:10], 'Readable download: ' + path.rsplit('/', 1)[-1],
                   ['recovered', 'repaired'] if r.get('file') else ['repaired'], 'Backup restoration' if r.get('file') else 'Encoding repair',
                   r['evidence'], 'The download is emitted as valid UTF-8, preserving its text and markup.',
                   [path], ['data/audit-repairs.json'])
    code_by_post = defaultdict(list)
    for r in recovery['code_blocks']:
        code_by_post[r['post_id']].append(r)
    for post_id, blocks in code_by_post.items():
        ids = {r['id'] for r in blocks}
        add_change('code-' + str(post_id), articles[post_id]['title'], ['repaired'], 'Legacy code plugin repaired',
                   'Unprocessed [code] markers, smart punctuation, or interpreted HTML obscured the intended example. In some articles, example tags also changed the surrounding layout.',
                   f'{len(blocks)} example(s) now display literal source with preserved quotes, hyphens and editorial emphasis. HTML, form, table and script examples do not execute.',
                   [p for p, page in pages.items() if page.codes & ids], ['data/recovery.json', 'data/code-block-review.json'])
    for post_id in sorted({r['post_id'] for r in ui['paragraph_code'] + ui['literal_markup']}):
        add_change('other-code-' + str(post_id), 'Code formatting: ' + articles[post_id]['title'], ['repaired'], 'Literal code restored',
                   'Paragraph-style code contained typographic punctuation or literal markup that the browser interpreted.',
                   'Code punctuation and formatting are repaired; example object/link tags stay visible without consuming article text.',
                   [articles[post_id]['path']], ['data/ui-repairs.json', 'data/code-block-review.json'])
    for gist in recovery['gists'].values():
        add_change('gist-' + str(gist['post_id']), 'Embedded code: ' + articles[gist['post_id']]['title'], ['preserved'], 'Inline copy at recorded revision',
                   'Displaying the example required a script from GitHub Gist.',
                   'The selected historical revision is now inline HTML: ' + ', '.join(f['name'] for f in gist['files']) + '.',
                   [gist['article']], ['data/recovery.json'])
    for r in recovery['tag_lists']:
        add_change('tags-' + str(r['post_id']), 'Readable tags: ' + articles[r['post_id']]['title'], ['repaired', 'preserved'], 'Plugin markup restored; destinations adapted',
                   'A broken SimpleTags shortcode exposed [tags] markers instead of the styled tag list.',
                   'The original small “Technorati Tags:” styling is restored. Tags lead to local topic indexes because the original Technorati destinations are retired.',
                   [r['article']], ['data/recovery.json', 'scripts/legacy.py'])
    for r in recovery['comments'] + recovery['comment_repairs']:
        restored = 'captured_text' not in r
        add_change('restored-comment-' + str(r['id']), ('Restored comment #' if restored else 'Completed pingback #') + str(r['id']), ['recovered'], 'Owner-approved backup recovery',
                   'The public capture did not contain this historical comment.' if restored else 'The current database/export already contained truncated text; this was not a display-length limit.',
                   'The approved 2007 backup text is restored with its authorship and existing links. Existing feed entries also carry the repair where applicable.',
                   [r['path']], ['data/recovery.json', 'data/comment-restoration-report.json'])
    for i, r in enumerate(recovery['demos']):
        path = r.get('path', r.get('local_path'))
        related = set(resource_users[path]) | {path}
        if r.get('article'):
            related.add(r['article'])
        add_change('demo-' + str(i), ['Table-height JavaScript demonstration', 'Aza Raskin’s undo demonstration', 'Interactive CSS button example'][i],
                   ['recovered', 'repaired', 'preserved'] if i != 2 else ['repaired'], 'Local adaptation',
                   ['The original script depended on a missing Prototype library.', 'The embedded Humanized demo was no longer available at its old URL.', 'The sample controls are for a local styling comparison, not server submissions.'][i],
                   r.get('behavior', r.get('status')), related, ['data/recovery.json', 'site/archive-assets/demos.js'])
    for path, tools in ui['bookmarklets'].items():
        add_change('tools-' + hashlib.sha256(path.encode()).hexdigest()[:8], f'{len(tools)} bookmarklets: ' + path.rsplit('/', 1)[-1],
                   ['recovered', 'repaired', 'preserved'], 'Recovered tools with local adaptations',
                   'Old tools depended on retired hosts, damaged markup or missing scripts and images.',
                   'Reviewed bookmarklets and dependencies are local; original attribution is retained. The retired PHP source viewer has a browser-only replacement. Browser policies can still restrict tools on other sites.',
                   {path} | resource_users[path], ['data/ui-repairs.json'], [r['id'] for r in resources if r['kind'] == 'Bookmarklet dependency' and path in r['pages']])
    add_change('podcast', 'Copenhagen Ruby Brigade podcast', ['recovered', 'repaired', 'preserved'], 'Same episode; publisher’s current encoding',
               'The old audio copy/player was unavailable.', audio['note'] + ' A native audio player and local MP3 are available from the article and both transcripts.',
               [articles[audio['post_id']]['path'], *audio['transcripts']], ['data/ui-repairs.json'])
    for r in data['video-players']:
        post = articles[r['post_id']]
        player = Page('/', r['replacement']).players[0]
        alternative = r.get('alternative')
        add_change('video-' + str(r['post_id']), player.get('title', post['title']), ['recovered'] if alternative else ['repaired'],
                   'Owner-approved replacement upload' if alternative else 'Native player migration',
                   'The embedded player or original hosting route no longer provided a usable player.',
                   'Uses a native YouTube player. ' + ('The replacement upload was reviewed and approved; it is not a byte-identical preservation claim. ' if alternative else 'The original video identifier is retained where supported. ') +
                   ('Original Mojiti annotations/transcription overlays are unavailable; the written transcript and screenshot remain. ' if 'mojiti' in r['captured'].lower() else '') +
                   ('The Danish recording was recovered from Internet Archive and uploaded to YouTube by the site owner. ' if '0nyF_4yMf28' in r['replacement'] else '') +
                   'Video playback still depends on YouTube; no video file is hosted in this archive.',
                   [post['path']], ['data/video-players.json'])
    for old, new in recovery['aliases'].items():
        add_change('asset-alias-' + hashlib.sha256(old.encode()).hexdigest()[:8], 'Repaired download: ' + old.rsplit('/', 1)[-1], ['recovered'], 'Existing original file relinked',
                   'The published link pointed to a missing old path.', 'The old path now serves the captured original file at ' + new + '.',
                   resource_users[old] | resource_users[new], ['data/recovery.json'])
    for media in content['media']:
        if media['id'] in audit['attachment_pages']:
            p = normalized(media['link'])
            add_change('attachment-' + str(media['id']), 'Attachment page: ' + plain(media['title']['rendered']), ['recovered'], 'Reconstructed from public media metadata',
                       'The original attachment display page did not return usable HTML.', 'The archive displays the recorded media with its public title.',
                       [p], ['data/audit-repairs.json', 'data/content.json'])
    for old, new in {**ui['redirects'], **audit['redirects']}.items():
        add_change('redirect-' + hashlib.sha256(old.encode()).hexdigest()[:8], 'Old address repaired: ' + old, ['repaired'], 'Canonical redirect',
                   'A historical or mistyped URL failed or relied on WordPress routing.', 'The static address redirects to ' + new + '.',
                   [old, new], ['data/ui-repairs.json', 'data/audit-repairs.json'])
    special = [
        ('homepage', 'Homepage pagination', ['/', '/archive/', *data['supplemental-capture']['pages']], 'The original homepage showed five posts, but its next page started at post 51.', '“More articles” now opens the full archive. Eight original pagination pages are also preserved.', ['data/supplemental-capture.json']),
        ('conditional-code', 'Visible conditional-comment example', [p for p, page in pages.items() if 'comment-455679' in page.ids], 'An HTML conditional-comment example was invisible because the browser treated it as markup.', 'The exact example is visible as code.', ['data/audit-repairs.json']),
        ('code-wrap', 'Long code stays inside the article', [p for p, page in pages.items() if 'archive-code' in page.classes or '<pre' in page.source or '<code' in page.source], 'Long code lines could extend into the sidebar or beyond the page.', 'Code can wrap within the article width without changing its source characters. This is a shared layout rule; not every listed page previously overflowed.', ['site/archive-assets/archive.css']),
        ('topics', 'Local topic indexes', [p for p, page in pages.items() if any(ref.startswith('/topics/') for ref in page.refs)], 'Technorati tag links depended on a retired service.', 'Topic links open local article indexes. Original WordPress tag archives and feed scopes remain separate.', ['scripts/legacy.py']),
    ]
    for key, title, paths, before, after, evidence in special:
        add_change(key, title, ['repaired', 'preserved'] if key == 'topics' else ['repaired'], 'Shared improvement' if key in ('code-wrap', 'topics') else 'Original-site defect repaired', before, after, paths, evidence, sitewide=key in ('code-wrap', 'topics'))

    for r in audit['excerpts']:
        text = re.sub(r'\s+', ' ', r['text'])
        locations = [p for p, page in pages.items() if text in re.sub(r'\s+', ' ', plain(page.source))]
        add_change('excerpt-' + str(r['post_id']), 'Readable excerpt: ' + articles[r['post_id']]['title'], ['repaired'], 'Shortcode and punctuation repair',
                   'Article-list excerpts exposed broken code shortcode markers and typographic command punctuation.',
                   'The reviewed excerpt displays readable code text and punctuation in the existing summary.',
                   locations, ['data/audit-repairs.json'])
    add_change('response-targets', 'Response anchors and unique form labels', ['repaired'], 'Shared validation and repair',
               'The comparison found missing response destinations and duplicate element IDs in original or converted markup.',
               'Response targets exist, form labels stay associated with their controls, and duplicate IDs are removed. The recorded repair pass fixed response destinations on 516 URLs; the list here shows all pages now covered by that rule, not 516 independently broken originals.',
               [p for p, page in pages.items() if 'comments' in page.ids or 'archive-form' in page.classes],
               ['data/audit-repair-report.json', 'scripts/reconcile.py'], sitewide=True)
    add_change('archived-forms', 'Visible forms with a clear submission notice', ['repaired'], 'Static migration adaptation',
               'Contact, comment and copied search forms required servers that the static archive does not run.',
               'Original fields remain visible, with a highlighted “This form no longer accepts submissions.” notice. These server forms are inert; separately reviewed local-only demos remain interactive.',
               [p for p, page in pages.items() if 'archive-form' in page.classes], ['README.md', 'scripts/archive.py'], sitewide=True)
    add_change('scoped-rss', 'RSS links retain their original paths and scope', ['preserved'], 'Static migration fidelity',
               'WordPress generated per-article responses and archive feeds dynamically. Early clone feed links did not retain all original scopes.',
               'Article footer links open their own response feeds at the original /feed/ paths. Category, tag and author feeds, plus 60 attachment-feed aliases, are generated locally. This preserves service behavior rather than recovering missing prose.',
               [r['path'] for r in articles.values()], ['data/comment-feeds.json', 'data/feed-aliases.json', 'scripts/feeds.py'], sitewide=True)
    add_change('feedburner-badge', 'FeedBurner badge replaced by a local RSS icon', ['repaired', 'preserved'], 'Visible replacement; original not recovered',
               'The retired FeedBurner image returned 404.',
               'A local RSS icon takes its place. The unavailable original badge is not counted as a recovered image.',
               resource_users['/archive-assets/feed.svg'], ['data/external-images.json', 'scripts/archive.py'], sitewide=True)

    # Link fixes refer back to public article/comment text, without importing
    # the private WordPress export or publishing its metadata.
    link_fixes = {**ui['external_link_repairs'], **audit['link_repairs'], **audit['reference_mappings']}
    affected = set()
    for row in content['posts'] + content['pages']:
        if any(old in html.unescape(row['content']['rendered']) for old in link_fixes):
            affected.add(articles[row['id']]['path'])
    for row in content['comments']:
        if row['post'] in articles and any(old in html.unescape(row['content']['rendered']) for old in link_fixes):
            affected.add(articles[row['post']]['path'])
    affected.update(audit['scoped_links'])
    add_change('malformed-links', 'Malformed links and demo navigation', ['repaired'], 'Recorded URL corrections',
               'Missing schemes, accidental relative paths and copied navigation sent readers to incorrect locations.',
               'The reviewed destinations are corrected. Ordinary external destination pages are still external, and this is not a recovery of those entire websites.',
               affected, ['data/ui-repairs.json', 'data/audit-repairs.json'])

    unresolved = [
        {'title': '18 external image references remain unavailable', 'detail': 'Native broken-image rendering is preserved, including alt text and dimensions. The retired FeedBurner badge is separately replaced by the local RSS icon.', 'evidence': 'data/ui-repair-report.json'},
        {'title': 'Missing decorative styles and legacy files', 'detail': '78 decorative-image URLs and two obsolete IE5 stylesheet imports were not recovered. Many decorations are unused banner variants. The exact train v6 demo, old spreadsheet stylesheet and IE6 PNG workaround also remain unavailable.', 'evidence': 'data/external-resources.json'},
        {'title': 'Flickr photo-page destinations remain external', 'detail': 'Embedded images are local. Thumbnail links to Flickr photo pages were deliberately retained; downloading the largest versions and changing those destinations is deferred.', 'evidence': 'README.md'},
        {'title': 'The screenshot audit still requires review', 'detail': 'The recorded full comparison covers 2,522 URLs and 1,704 browser pairs. Its 1,076 URLs with pending visual differences are not 1,076 confirmed defects. Three articles have image-layout differences specifically left for review. This ledger is not a passing pixel-equivalence certificate.', 'evidence': 'data/audit-summary.json'},
        {'title': 'Hosted players and historical interaction limits', 'detail': 'YouTube remains an intentional external dependency. Mojiti overlays are lost. Forms needing WordPress no longer submit; browser-only demonstrations remain interactive.', 'evidence': 'data/video-players.json'},
    ]
    page_changes = defaultdict(set)
    for change in changes:
        for path in change['pages']:
            page_changes[path].add(change['id'])
    # Shared, archive-wide adaptations are reported separately so they do not
    # inflate the count of pages with a specific recovery or repair.
    specific = {p for c in changes if not c['sitewide'] for p in c['pages']}
    index = [dict(describe_page(p), changes=sorted(ids), canonical=family(p), primary=primary(p))
             for p, ids in sorted(page_changes.items())]
    return {'schema_version': 1, 'evidence_date': '2026-10-23',
            'inputs': {f'data/{name}.json': hashlib.sha256((ROOT / f'data/{name}.json').read_bytes()).hexdigest() for name in INPUTS},
            'counts': {'documented_changes': len(changes), 'specific_html_urls': len(specific),
                       'primary_pages_with_specific_changes': sum(primary(p) for p in specific),
                       'local_resource_records': len(resources), 'unique_local_files_or_inline_pages': len({r['path'] for r in resources}),
                       'resource_kinds': dict(sorted(Counter(r['kind'].split(':')[0] for r in resources).items())),
                       'code_examples': len(recovery['code_blocks']), 'code_articles': len(code_by_post),
                       'gist_embeds': len(recovery['gists']), 'gist_files': sum(len(g['files']) for g in recovery['gists'].values()),
                       'video_replacement_posts': sum(bool(r.get('alternative')) for r in data['video-players'])},
            'changes': sorted(changes, key=lambda c: c['title'].casefold()),
            'resources': sorted(resources, key=lambda r: (r['kind'], r['source'])),
            'pages': index, 'unresolved': unresolved,
            'scope': 'Public reviewed recovery manifests and the generated archive. Includes every located HTML occurrence of recorded resources, plus explicit reviewed owners for inline gists and dynamic bookmarklet bundles. Resource users include direct links as well as embedded loads. Archive/listing copies are separated from primary articles and demos. Shared bookmarklet dependencies are attributed to their toolbox bundle, not claimed as individually exercised on each page.'}


def esc(value):
    return html.escape(str(value), quote=True)


def link(url, label):
    marker = ' data-migration-reference="true"' if urlsplit(url).scheme in ('http', 'https') else ''
    return f'<a href="{esc(url)}"{marker}>{esc(label)}</a>'


def page_links(paths, pages):
    preferred = [p for p in paths if pages[p]['primary']]
    other = [p for p in paths if not pages[p]['primary']]
    def items(group):
        return '<ul class="page-links">' + ''.join(f'<li>{link(p, pages[p]["title"])} <small>{link(pages[p]["original_url"], "Original")}</small></li>' for p in group) + '</ul>'
    output = items(preferred) if preferred else ''
    if other:
        output += f'<details><summary>{len(other)} archive, pagination or alternate URL(s)</summary>{items(other)}</details>'
    return output or '<p class="muted">Preserved in the resource bundle; no direct HTML occurrence was located.</p>'


def render(report):
    counts = report['counts']
    pages = {p['path']: p for p in report['pages']}
    resources = {r['id']: r for r in report['resources']}
    changes = {c['id']: c for c in report['changes']}
    parts = [f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Migration &amp; preservation report | justaddwater.dk</title>
<meta name="description" content="A page-by-page record of recovered content, repaired rendering and locally preserved resources in the justaddwater.dk archive.">
<link rel="stylesheet" href="/archive-assets/migration-report.css"><script defer src="/archive-assets/migration-report.js"></script></head><body>
<a class="skip" href="#changes">Skip to the change inventory</a><header><a href="/">justaddwater.dk</a><span>Archive record / 23 October 2026</span></header>
<main><section class="intro"><div><h1>Recovered, repaired,<br>preserved.</h1>
<p class="lead">What we brought back while moving justaddwater.dk from WordPress to a static archive.</p>
<p>Some material survived only in backups or web archives. Some was still there, hidden by broken plugins. Other resources worked, but relied on someone else’s server. This report keeps those stories separate.</p>
<nav aria-label="Report sections"><a href="#changes">Changes</a><a href="#pages">Every affected page</a><a href="#resources">Local resource inventory</a><a href="#limits">Still missing &amp; deferred</a></nav></div>
<aside class="ledger"><h2>In the record</h2><dl><div><dt>Articles and demos with specific changes</dt><dd>{counts['primary_pages_with_specific_changes']}</dd></div><div><dt>Code examples repaired</dt><dd>{counts['code_examples']}</dd></div><div><dt>Gist files preserved inline</dt><dd>{counts['gist_files']}</dd></div><div><dt>Local resource records</dt><dd>{counts['local_resource_records']}</dd></div></dl><p>Counts overlap. A recovered image can also be a locally preserved resource. Source URLs can share one file.</p></aside></section>
<section class="reading"><h2>Three kinds of improvement</h2><div class="definitions"><p><b class="recovered">Recovered content</b> Material recovered from backups, archives or an approved replacement upload. Adaptations and replacements are labeled.</p><p><b class="repaired">Rendering &amp; behavior</b> Code, tags, layout and demos that now display or behave as their surviving source intended.</p><p><b class="preserved">Kept locally</b> Files or inline content that no longer need their former external host. YouTube videos are not counted here.</p></div></section>
<section id="changes"><div class="section-heading"><h2>The change inventory</h2><p>{counts['documented_changes']} documented changes or groups</p></div>
<div class="filters" data-filter-group="changes"><label>Find a change<input type="search" id="change-query" placeholder="Try Google menus, tags, podcast, table…"></label><label>Show<select id="change-kind"><option value="">All improvements</option>{''.join(f'<option value="{k}">{esc(v)}</option>' for k,v in CATEGORIES.items())}</select></label><label class="check"><input id="shared-changes" type="checkbox" checked> Include shared site improvements</label><output id="change-count" aria-live="polite"></output></div>
<noscript><p>All entries are shown below. Browser JavaScript enables filtering only.</p></noscript><div class="change-list">''']
    for c in report['changes']:
        assets = [resources[i] for i in c['resources']]
        searchable = ' '.join([c['title'], c['before'], c['after'], c['outcome'], *c['pages'], *(pages[p]['title'] for p in c['pages']), *(r['source'] + ' ' + r['note'] for r in assets)])
        parts.append(f'<article class="change" id="{c["id"]}" data-categories="{" ".join(c["categories"])}" data-shared="{str(c["sitewide"]).lower()}" data-search="{esc(searchable.lower())}"><div class="change-label"><span>{esc(c["outcome"])}</span>{"".join(f"<b class={k}>{esc(CATEGORIES[k])}</b>" for k in c["categories"])}</div><div><h3>{esc(c["title"])}</h3><div class="before-after"><p><strong>Before</strong>{esc(c["before"])}</p><p><strong>In the archive</strong>{esc(c["after"])}</p></div>')
        parts.append(f'<details class="locations"><summary>Where to see it ({len(c["pages"])} HTML URLs)</summary>{page_links(c["pages"], pages)}</details>')
        if assets:
            parts.append(f'<details><summary>Preserved resources ({len(assets)})</summary><ul>' + ''.join(f'<li>{link("#" + r["id"], r["source"])}</li>' for r in assets) + '</ul></details>')
        parts.append('<p class="evidence">Records: ' + ', '.join(link(REPO + f, f.removeprefix('data/')) for f in c['evidence']) + '</p></div></article>')
    parts.append('</div><p class="empty" id="changes-empty" hidden>No matching changes. Try a shorter search or another category.</p></section>')
    parts.append(f'''<section id="pages"><div class="section-heading"><h2>Every affected page</h2><p>Articles, demos and their archived copies</p></div><p>The default view lists original articles, pages and demonstrations. Include archive copies to see category listings, pagination and comment-page URLs. Shared changes such as code wrapping do not imply that every listed page originally had a visible defect.</p>
<div class="filters"><label>Find a page<input id="page-query" type="search" placeholder="Page title or URL"></label><label class="check"><input id="page-copies" type="checkbox"> Include archive and alternate pages</label><output id="page-count" aria-live="polite"></output></div><div class="table-wrap"><table><thead><tr><th scope="col">Page</th><th scope="col">Documented changes</th></tr></thead><tbody>''')
    for p in report['pages']:
        parts.append(f'<tr class="page-row" data-primary="{str(p["primary"]).lower()}" data-search="{esc((p["title"] + " " + p["path"]).lower())}"><td>{link(p["path"],p["title"])}<small>{esc(p["path"])}</small>{link(p["original_url"], "Original site")}</td><td><ul>' + ''.join(f'<li>{link("#"+c,changes[c]["title"])}</li>' for c in p['changes']) + '</ul></td></tr>')
    parts.append('</tbody></table></div><p class="empty" id="pages-empty" hidden>No matching pages.</p></section>')
    kinds = sorted({r['kind'].split(':')[0] for r in report['resources']})
    parts.append(f'''<section id="resources"><div class="section-heading"><h2>The local resource inventory</h2><p>{counts['local_resource_records']} source records</p></div><p>Each entry records the old dependency, its local copy or inline location, the recovery source, and where it is used. This includes direct image links and CSS dependencies. It excludes missing files and externally hosted videos. Gist entries point to the containing article; bookmarklet dependencies list their shared toolbox bundle.</p><div class="filters"><label>Find a resource<input type="search" id="resource-query" placeholder="Host, filename or page"></label><label>Type<select id="resource-kind"><option value="">All resource types</option>{''.join(f'<option>{esc(k)}</option>' for k in kinds)}</select></label><output id="resource-count" aria-live="polite"></output></div><div class="resource-list">''')
    for r in report['resources']:
        known = [p for p in r['pages'] if p in pages]
        search = ' '.join([r['source'],r['path'],r['note'],r['outcome'],*(pages[p]['title'] for p in known),*known]).lower()
        parts.append(f'<details class="resource" id="{r["id"]}" data-kind="{esc(r["kind"].split(":")[0])}" data-search="{esc(search)}"><summary><span>{esc(r["kind"])}</span><b>{esc(r["source"])}</b><small>{esc(r["outcome"])}</small></summary><div class="resource-body"><p>{link(r["path"],"Open local copy" if not r["kind"].startswith("Inline") else "Read the inline code")} / {link(r["source"],"Original source")}' + (' / ' + link(r['retrieved_from'],'Recovery source') if r['retrieved_from'] else '') + f'</p><p>{esc(r["note"])}</p>{page_links(known,pages)}<p class="evidence">{link(REPO + r["evidence"],"Recovery record")}' + (f' / SHA-256 <code>{esc(r["sha256"])}</code>' if r['sha256'] else '') + '</p></div></details>')
    parts.append('</div><p class="empty" id="resources-empty" hidden>No matching resources.</p></section>')
    parts.append('<section id="limits"><h2>Still missing, adapted or deferred</h2><p>A record of improvements should also make the limits easy to find.</p><dl class="limitations">' + ''.join(f'<div><dt>{esc(r["title"])}</dt><dd>{esc(r["detail"])} {link(REPO+r["evidence"],"Record")}</dd></div>' for r in report['unresolved']) + '</dl>')
    parts.append('<details><summary>Image-layout differences specifically left for review</summary><ul>' + ''.join(f'<li>{link(p,"Open archive: " + p)} / {link("http://justaddwater.dk"+p,"Original")}</li>' for p in json.loads((ROOT/'data/audit-new-findings.json').read_text())['image_layout_articles']) + '</ul></details></section>')
    parts.append('''<section id="method"><h2>About this record</h2><p>This report consolidates the reviewed recovery manifests and indexes the generated HTML and CSS. It does not fetch or publish the private WordPress XML, database dump, drafts, email addresses or IP metadata. The evidence dates from the migration on 22–23 October 2026; links to the original site are for comparison and may degrade later.</p><p>Routine migration changes are recorded in the README: static search and scoped feeds, retained but non-submitting forms, updated footer wording, response anchors, removal of duplicate IDs and tracking scripts, and locally served theme assets. Those are not counted as newly recovered historical content.</p><p>The detailed screenshot audit remains local because it is large and tied to the capture cache. Its public summary is linked here; this report does not replace it or automatically approve its outstanding visual reviews.</p><p>'''+link('/migration-report/report.json','Download the complete JSON inventory')+' / '+link(REPO+'README.md','Migration notes and audit instructions')+' / '+link(REPO+'scripts/migration_report.py','Report generator')+'</p></section></main><footer>justaddwater.dk archive / Evidence preserved with the '+link('https://github.com/watson/justaddwater.dk','source repository')+'</footer></body></html>')
    return '\n'.join(parts) + '\n'


def generate(check=False):
    report = build_report()
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    outputs = {ROOT / 'data/migration-report.json': encoded,
               SITE / 'migration-report/report.json': encoded,
               SITE / 'migration-report/index.html': render(report)}
    for path, text in outputs.items():
        if check:
            if not path.exists() or path.read_text() != text:
                raise SystemExit('Migration report is stale: ' + str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
    print(json.dumps(report['counts'], indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if committed report differs from its public inputs and site.')
    generate(parser.parse_args().check)
