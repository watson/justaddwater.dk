"""Static RSS feeds with the same directory URLs as the WordPress site."""
from datetime import datetime, timezone
from email.utils import format_datetime, parsedate_to_datetime
import html
import json
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlsplit, urlunsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from recovery import recovery_data, restore_comment_content

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://justaddwater.dk'
ATOM = 'http://www.w3.org/2005/Atom'
CONTENT = 'http://purl.org/rss/1.0/modules/content/'
DC = 'http://purl.org/dc/elements/1.1/'
ET.register_namespace('atom', ATOM)
ET.register_namespace('content', CONTENT)
ET.register_namespace('dc', DC)


def url_path(url):
    return quote(unquote(urlsplit(url).path), safe="/!$&'()*+,-.;=@_~")


def is_feed(path):
    # WordPress interprets even the apparent "rss" and "atom" category slugs
    # as legacy feed aliases, redirecting to the parent category's feed.
    return bool(re.search(r'/(?:feed|rss2?|atom)/?$', path))


def feed_specs(data, comment_paths=None):
    specs = {
        '/feed/': {'kind': 'posts', 'title': 'justaddwater.dk', 'home': '/', 'posts': data['posts'][:50]},
        '/comments/feed/': {'kind': 'comments', 'title': 'Comments for justaddwater.dk', 'home': '/'},
    }
    for kind in ('posts', 'pages', 'media'):
        for row in data[kind]:
            path = url_path(row['link'])
            if not path.endswith('/'):
                continue
            if comment_paths is not None and path + 'feed/' not in comment_paths:
                continue
            specs[path + 'feed/'] = {
                'kind': 'comments', 'post_id': row['id'], 'home': path,
                'title': 'Comments on: ' + BeautifulSoup('<span>' + row['title']['rendered'] + '</span>', 'html.parser').get_text(),
            }
    for kind, field in [('categories', 'categories'), ('tags', 'tags'), ('users', 'author')]:
        for row in data[kind]:
            matches = {row['id']}
            if kind == 'categories':
                while True:
                    expanded = matches | {c['id'] for c in data[kind] if c['parent'] in matches}
                    if expanded == matches:
                        break
                    matches = expanded
            posts = [p for p in data['posts'] if (p[field] in matches if field == 'author' else bool(matches.intersection(p[field])))]
            path = url_path(row['link']).rstrip('/') + '/'
            specs[path + 'feed/'] = {'kind': 'posts', 'title': html.unescape(row['name']) + ' – justaddwater.dk',
                                    'home': path, 'posts': posts[:10]}
    parent = '/category/webstandards/feed/'
    if parent in specs:
        specs[parent + 'atom/'] = {**specs[parent], 'format': 'atom'}
        specs['/category/webstandards/rss/'] = specs[parent]
        specs['/category/webstandards/atom/'] = specs[parent + 'atom/']
    for path in json.loads((ROOT / 'data/feed-aliases.json').read_text())['aliases']:
        specs[path] = {**specs['/feed/'], 'posts': data['posts'][:10]}
    return specs


def parse_comment_feed(raw):
    """Keep only public RSS fields; never import WordPress account metadata."""
    channel = ET.fromstring(raw).find('channel')
    if channel is None:
        raise ValueError('Expected an RSS channel')
    items = []
    for node in channel.findall('item'):
        link = node.findtext('link', '').strip()
        match = re.search(r'#comment-(\d+)$', link)
        if not match:
            raise ValueError('Expected a comment permalink: ' + link)
        items.append({'id': int(match[1]), 'title': node.findtext('title', '').strip(),
                      'author': node.findtext(f'{{{DC}}}creator', '').strip(), 'link': link,
                      'guid': node.findtext('guid', '').strip(), 'date': node.findtext('pubDate', '').strip(),
                      'content': node.findtext(f'{{{CONTENT}}}encoded') or node.findtext('description', '')})
    return items


def comment_items(spec, data, snapshots):
    if 'post_id' in spec:
        items = list(snapshots['feeds'][spec['home'] + 'feed/']['items'])
    else:
        by_id = {item['id']: item for feed in snapshots['feeds'].values() for item in feed['items']}
        for c in data['comments']:
            by_id.setdefault(c['id'], {'id': c['id'], 'title': 'By: ' + c['author_name'], 'author': c['author_name'],
                                      'link': c['link'], 'guid': re.sub(r'/comment-page-\d+/', '/', c['link']),
                                      'date': format_datetime(datetime.fromisoformat(c['date_gmt']).replace(tzinfo=timezone.utc)),
                                      'content': c['content']['rendered']})
        items = list(by_id.values())
    for c in recovery_data()['comments']:
        if 'post_id' in spec and c['post_id'] != spec['post_id']:
            continue
        if any(i['id'] == c['id'] for i in items):
            continue
        items.append({'id': c['id'], 'title': ('Pingback: ' if c['type'] == 'pingback' else 'By: ') + c['author'],
                      'author': c['author'], 'link': 'http://justaddwater.dk' + c['path'] + f'#comment-{c["id"]}',
                      'guid': 'http://justaddwater.dk' + c['path'] + f'#comment-{c["id"]}',
                      'date': format_datetime(datetime.fromisoformat(c['date_gmt']).replace(tzinfo=timezone.utc)),
                      'content': '<p>' + html.escape(c['content']) + '</p>'})
    selected = sorted(items, key=lambda i: (parsedate_to_datetime(i['date']), i['id']), reverse=True)[:10 if 'post_id' in spec else 50]
    return [{**item, 'content': restore_comment_content(item['id'], item['content'])} for item in selected]


def write_feeds(data, site, render_content, snapshots=None, comment_links=None):
    if snapshots is None:
        snapshots = json.loads((ROOT / 'data/comment-feeds.json').read_text())
    specs = feed_specs(data, snapshots['feeds'])
    post_guids = json.loads((ROOT / 'data/post-feed-ids.json').read_text())
    users = {u['id']: u['name'] for u in data['users']}
    for path, spec in specs.items():
        items = comment_items(spec, data, snapshots) if spec['kind'] == 'comments' else [
            {'title': html.unescape(p['title']['rendered']), 'link': p['link'], 'guid': post_guids[str(p['id'])],
             'author': users.get(p['author'], ''), 'content': p['content']['rendered'],
             'date': format_datetime(datetime.fromisoformat(p['date_gmt']).replace(tzinfo=timezone.utc))}
            for p in spec['posts']]
        target = site / unquote(path).lstrip('/') / 'index.xml'
        target.parent.mkdir(parents=True, exist_ok=True)
        if spec.get('format') == 'atom':
            feed = ET.Element(f'{{{ATOM}}}feed')
            ET.SubElement(feed, f'{{{ATOM}}}title').text = spec['title']
            ET.SubElement(feed, f'{{{ATOM}}}id').text = ORIGIN + spec['home'] + 'feed/atom/'
            ET.SubElement(feed, f'{{{ATOM}}}link', href=ORIGIN + path, rel='self', type='application/atom+xml')
            ET.SubElement(feed, f'{{{ATOM}}}link', href=ORIGIN + spec['home'], rel='alternate')
            ET.SubElement(feed, f'{{{ATOM}}}updated').text = parsedate_to_datetime(items[0]['date']).isoformat()
            for row in items:
                entry = ET.SubElement(feed, f'{{{ATOM}}}entry')
                ET.SubElement(entry, f'{{{ATOM}}}title').text = row['title']
                ET.SubElement(entry, f'{{{ATOM}}}id').text = row['guid']
                ET.SubElement(entry, f'{{{ATOM}}}link', href=row['link'], rel='alternate')
                author = ET.SubElement(entry, f'{{{ATOM}}}author')
                ET.SubElement(author, f'{{{ATOM}}}name').text = row['author']
                ET.SubElement(entry, f'{{{ATOM}}}updated').text = parsedate_to_datetime(row['date']).isoformat()
                ET.SubElement(entry, f'{{{ATOM}}}content', type='html').text = render_content(row['content'], row['link'])
            ET.ElementTree(feed).write(target, encoding='utf-8', xml_declaration=True)
            continue
        rss = ET.Element('rss', version='2.0')
        channel = ET.SubElement(rss, 'channel')
        ET.SubElement(channel, 'title').text = spec['title']
        ET.SubElement(channel, 'link').text = ORIGIN + spec['home']
        ET.SubElement(channel, 'description').text = 'Instant Usability & Web Standards — static archive'
        ET.SubElement(channel, 'language').text = 'en-US'
        ET.SubElement(channel, f'{{{ATOM}}}link', href=ORIGIN + path, rel='self', type='application/rss+xml')
        for row in items:
            item = ET.SubElement(channel, 'item')
            for name in ('title', 'link'):
                value = row[name]
                if name == 'link' and spec['kind'] == 'comments' and comment_links is not None:
                    value = ORIGIN + comment_links[row['id']] + f'#comment-{row["id"]}'
                ET.SubElement(item, name).text = value
            ET.SubElement(item, 'guid', isPermaLink='false').text = row['guid']
            ET.SubElement(item, f'{{{DC}}}creator').text = row['author']
            ET.SubElement(item, 'pubDate').text = row['date']
            ET.SubElement(item, 'description').text = render_content(row['content'], row['link'])
        ET.ElementTree(rss).write(target, encoding='utf-8', xml_declaration=True)
    return specs


def deploy_feed(text, site_url):
    """Use the deployed origin for navigable URLs, retaining original GUIDs."""
    root = ET.fromstring(text)

    def url(value):
        parts = urlsplit(value)
        if parts.hostname in ('justaddwater.dk', 'www.justaddwater.dk'):
            return site_url.rstrip('/') + urlunsplit(('', '', parts.path, parts.query, parts.fragment))
        if value.startswith('/') and not value.startswith('//'):
            return site_url.rstrip('/') + value
        return value

    for node in root.iter():
        if node.tag == 'link' and node.text:
            node.text = url(node.text)
        elif node.tag == f'{{{ATOM}}}link' and node.get('href'):
            node.set('href', url(node.get('href')))
        elif node.tag in ('description', f'{{{CONTENT}}}encoded', f'{{{ATOM}}}content') and node.text:
            soup = BeautifulSoup(node.text, 'html.parser')
            for tag in soup.find_all(True):
                for attr in ('href', 'src', 'poster'):
                    if tag.get(attr):
                        tag[attr] = url(tag[attr])
                if tag.get('srcset'):
                    tag['srcset'] = ', '.join(' '.join([url(parts[0]), *parts[1:]])
                                             for value in tag['srcset'].split(',') if (parts := value.split()))
                if tag.get('style'):
                    tag['style'] = re.sub(r'url\([\"\']?(/[^)\"\']*)[\"\']?\)',
                                          lambda m: 'url("' + url(m[1]) + '")', tag['style'])
            node.text = str(soup)
    return ET.tostring(root, encoding='utf-8', xml_declaration=True).decode()
