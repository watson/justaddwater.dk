import copy
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from archive import ROOT, ORIGIN, local_url, rewrite, parse_document
from feeds import ATOM, feed_specs, is_feed, parse_comment_feed, write_feeds, deploy_feed
from prepare_pages import PrefixHTML


class FeedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'data/content.json').read_text())
        cls.snapshots = json.loads((ROOT / 'data/comment-feeds.json').read_text())
        cls.post_guids = json.loads((ROOT / 'data/post-feed-ids.json').read_text())
        cls.cookie = '/2007/01/29/javascript-cookie-editor-bookmarklet/'

    def test_article_feed_path_survives_rewrite_and_project_prefixing(self):
        path = self.cookie + 'feed/'
        for source in [ORIGIN + path, ORIGIN + '/?feed=rss2&p=523', ORIGIN + self.cookie + '?feed=rss2']:
            with self.subTest(source=source):
                self.assertEqual(local_url(source, ORIGIN, {'523': self.cookie}), path)
                soup = rewrite(parse_document(f'<a href="{source}">RSS 2.0</a>'), ORIGIN, {'523': self.cookie}, {path}, set())
                parser = PrefixHTML('/justaddwater.dk')
                parser.feed(str(soup)); parser.close()
                output = BeautifulSoup(''.join(parser.parts), 'html.parser')
                self.assertEqual(output.a['href'], '/justaddwater.dk' + path)

    def test_legacy_category_feed_aliases_keep_the_parent_category_scope(self):
        specs = feed_specs(self.data, self.snapshots['feeds'])
        for name in ('rss', 'atom'):
            path = f'/category/webstandards/{name}/'
            self.assertTrue(is_feed(path))
            self.assertTrue(is_feed(path + 'feed/'))
            self.assertEqual(specs[path]['posts'], specs['/category/webstandards/feed/']['posts'])
            soup = rewrite(parse_document(f'<a href="{ORIGIN}{path}">Category</a>'), ORIGIN, {}, {path}, set())
            self.assertEqual(soup.a['href'], path)
        self.assertEqual(specs['/category/webstandards/atom/']['format'], 'atom')

    def test_scoped_feeds_only_contain_matching_posts_and_include_child_categories(self):
        specs = feed_specs(self.data, self.snapshots['feeds'])
        self.assertEqual(len(specs[self.cookie + 'feed/'].get('posts', [])), 0)
        for kind, field in [('tags', 'tags'), ('users', 'author')]:
            row = self.data[kind][0]
            posts = specs[row['link'].removeprefix(ORIGIN) + 'feed/']['posts']
            self.assertTrue(posts)
            self.assertTrue(all(p[field] == row['id'] if field == 'author' else row['id'] in p[field] for p in posts))
        parent = next(c for c in self.data['categories'] if c['slug'] == 'webstandards')
        posts = specs[parent['link'].removeprefix(ORIGIN) + 'feed/']['posts']
        child_ids = {c['id'] for c in self.data['categories'] if c['parent'] == parent['id']}
        self.assertTrue(any(child_ids.intersection(p['categories']) for p in posts))

    def test_original_cookie_feed_preserves_all_nine_comment_ids_and_dates(self):
        feed = self.snapshots['feeds'][self.cookie + 'feed/']
        original = [c for c in self.data['comments'] if c['post'] == 523]
        self.assertEqual({i['id'] for i in feed['items']}, {c['id'] for c in original})
        self.assertEqual(len(feed['items']), 9)
        self.assertEqual(feed['items'][0]['date'], 'Mon, 23 Jun 2008 18:33:51 +0000')
        self.assertEqual(feed['items'][0]['guid'], ORIGIN + self.cookie + '#comment-425822')

    def test_each_feed_is_xml_at_its_original_directory_with_no_html_redirect(self):
        data = copy.deepcopy(self.data)
        data['posts'] = [p for p in data['posts'] if p['id'] in (523, 718)]
        for kind in ('pages', 'media', 'categories', 'tags', 'users'):
            data[kind] = []
        snapshots = {'feeds': {self.cookie + 'feed/': self.snapshots['feeds'][self.cookie + 'feed/'],
                               '/2007/09/27/undo-not-confirmation-end-of-discussion/feed/': {'items': []}}}
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            write_feeds(data, site, lambda text, base: text, snapshots)
            file = site / self.cookie.strip('/') / 'feed/index.xml'
            self.assertFalse(file.with_name('index.html').exists())
            original = ET.parse(file).getroot()
            channel = original.find('channel')
            self.assertEqual(channel.findtext('title'), 'Comments on: Handy JavaScript Cookie Editor')
            self.assertEqual(len(channel.findall('item')), 9)
            deployed = ET.fromstring(deploy_feed(file.read_text(), 'https://watson.github.io/justaddwater.dk'))
            self.assertEqual(deployed.find(f'./channel/{{{ATOM}}}link').get('href'),
                             'https://watson.github.io/justaddwater.dk' + self.cookie + 'feed/')
            self.assertEqual([i.findtext('guid') for i in deployed.findall('./channel/item')],
                             [i.findtext('guid') for i in channel.findall('item')])
            self.assertTrue(all(i.findtext('link').startswith('https://watson.github.io/justaddwater.dk' + self.cookie)
                                for i in deployed.findall('./channel/item')))
            empty = ET.parse(site / '2007/09/27/undo-not-confirmation-end-of-discussion/feed/index.xml')
            self.assertEqual(empty.getroot().findall('./channel/item'), [])

    def test_deployment_rewrites_embedded_links_but_not_example_text_or_guids(self):
        root = ET.Element('rss'); channel = ET.SubElement(root, 'channel'); item = ET.SubElement(channel, 'item')
        ET.SubElement(item, 'guid').text = ORIGIN + '/?p=1'
        ET.SubElement(item, 'description').text = '<a href="http://justaddwater.dk/a/">A</a><img src="/photo.png"><code>http://justaddwater.dk/example/</code>'
        deployed = ET.fromstring(deploy_feed(ET.tostring(root, encoding='unicode'), 'https://example.com/archive'))
        self.assertEqual(deployed.findtext('./channel/item/guid'), ORIGIN + '/?p=1')
        body = BeautifulSoup(deployed.findtext('./channel/item/description'), 'html.parser')
        self.assertEqual(body.a['href'], 'https://example.com/archive/a/')
        self.assertEqual(body.img['src'], 'https://example.com/archive/photo.png')
        self.assertEqual(body.code.get_text(), 'http://justaddwater.dk/example/')

    def test_comment_capture_rejects_a_main_posts_feed(self):
        with self.assertRaisesRegex(ValueError, 'Expected a comment permalink'):
            parse_comment_feed('<rss><channel><item><link>http://justaddwater.dk/article/</link></item></channel></rss>')

    def test_original_atom_aliases_remain_atom_and_use_deployed_links(self):
        data = {**self.data, 'pages': [], 'media': [], 'tags': [], 'users': [], 'comments': []}
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            specs = write_feeds(data, site, lambda text, base: text, {'feeds': {}})
            for path in ('/category/webstandards/atom/', '/category/webstandards/feed/atom/'):
                file = site / path.strip('/') / 'index.xml'
                root = ET.fromstring(deploy_feed(file.read_text(), 'https://example.com/archive'))
                self.assertEqual(root.tag, f'{{{ATOM}}}feed')
                self.assertEqual(root.find(f'{{{ATOM}}}link[@rel="self"]').get('href'), 'https://example.com/archive' + path)
                entries = root.findall(f'{{{ATOM}}}entry')
                self.assertEqual([e.findtext(f'{{{ATOM}}}id') for e in entries], [self.post_guids[str(p['id'])] for p in specs[path]['posts']])
                self.assertTrue(all(e.find(f'{{{ATOM}}}link').get('href').startswith('https://example.com/archive/') for e in entries))

    def test_comment_links_use_preserved_html_locations_without_changing_guids(self):
        data = {**self.data, 'posts': [p for p in self.data['posts'] if p['id'] == 523],
                'pages': [], 'media': [], 'categories': [], 'tags': [], 'users': [], 'comments': []}
        snapshots = {'feeds': {self.cookie + 'feed/': self.snapshots['feeds'][self.cookie + 'feed/']}}
        links = {i['id']: self.cookie for i in snapshots['feeds'][self.cookie + 'feed/']['items']}
        links.update({27244: '/archive/', 58286: '/attachment/'})
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            write_feeds(data, site, lambda text, base: text, snapshots, links)
            items = ET.parse(site / self.cookie.strip('/') / 'feed/index.xml').findall('./channel/item')
            for item in items:
                fragment = item.findtext('guid').split('#')[1]
                self.assertEqual(item.findtext('link'), 'https://justaddwater.dk' + self.cookie + '#' + fragment)
                self.assertTrue(item.findtext('guid').startswith(ORIGIN))


if __name__ == '__main__':
    unittest.main()
