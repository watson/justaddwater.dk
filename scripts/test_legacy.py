import hashlib
import html
import json
import unittest
from urllib.parse import urlsplit

from bs4 import BeautifulSoup

from archive import ROOT, ORIGIN, clean_html, parse_document, local_url, rewrite, id_routes
from legacy import ui_repairs, topic_index, topic_body
from prepare_pages import PrefixHTML
from verify import article_text_preserved


class LegacyUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / 'data/content.json').read_text())
        cls.posts = {row['id']: row for row in data['posts']}

    def test_ie7_literal_tags_preserve_prose_without_creating_elements(self):
        source = self.posts[384]['content']['rendered']
        soup = clean_html(parse_document(source))
        text = ' '.join(soup.get_text(' ', strip=True).split())
        self.assertIn('<object> tag no longer limited to 128 characters', text)
        self.assertIn('<object> fallback', text)
        self.assertIn('Enable :hover on all elements not just on <a>', text)
        self.assertIsNone(soup.object)
        self.assertTrue(article_text_preserved(source, text))
        self.assertFalse(article_text_preserved(source, text.replace('tag no longer limited to 128 characters', '')))
        self.assertFalse(article_text_preserved(source, text.replace('fallback', '')))

    def test_paragraph_examples_preserve_prose_and_render_literal_code(self):
        for post_id in {row['post_id'] for row in ui_repairs()['paragraph_code']}:
            with self.subTest(post=post_id):
                source = self.posts[post_id]['content']['rendered']
                soup = clean_html(parse_document(source))
                for row in ui_repairs()['paragraph_code']:
                    if row['post_id'] != post_id:
                        continue
                    code = soup.find(attrs={'data-repair-code': row['id']})
                    self.assertEqual(code.get_text(), row['code'])
                    self.assertIsNone(code.find(['form', 'script', 'a']))
                actual = ' '.join(soup.get_text(' ', strip=True).split())
                self.assertTrue(article_text_preserved(source, actual))
        command = next(r['code'] for r in ui_repairs()['paragraph_code'] if r['post_id'] == 1733)
        self.assertIn('--env-filter', command)
        self.assertIn('-- --all', command)
        self.assertNotRegex(command, '[“”‘’–—]')

    def test_only_exact_reviewed_bookmarklets_survive_cleanup_and_prefixing(self):
        for path, records in ui_repairs()['bookmarklets'].items():
            raw = '<html><head></head><body>' + ''.join('<a href="' + html.escape(r['captured'], quote=True) + '">' + html.escape(r['label']) + '</a>' for r in records) + '</body></html>'
            soup = clean_html(parse_document(raw), path=path)
            parser = PrefixHTML('/justaddwater.dk')
            parser.feed(str(soup)); parser.close()
            result = BeautifulSoup(''.join(parser.parts), 'html.parser')
            for row in records:
                link = result.find(attrs={'data-archive-bookmarklet': row['id']})
                self.assertIsNotNone(link)
                self.assertEqual(link['href'], row['replacement'])
            altered = '<a data-archive-bookmarklet="' + records[0]['id'] + '" href="javascript:alert(1)">Unexpected</a>'
            self.assertIsNone(clean_html(parse_document(altered), path=path).a.get('href'))
            self.assertFalse(clean_html(parse_document(raw), path='/unrelated/').select('a[href^="javascript:"]'))

    def test_technorati_links_target_complete_local_topic_indexes(self):
        topics = topic_index()
        soup = clean_html(parse_document(self.posts[718]['content']['rendered']))
        result = rewrite(soup, ORIGIN, {}, {r['path'] for r in topics.values()}, set())
        links = result.select('[data-recovery-tags] a')
        self.assertEqual([a['href'] for a in links], [topics[k]['path'] for k in ['asa raskin', 'usability', 'undo', 'confirmation']])
        self.assertTrue(all(a['data-original-url'].startswith('http://technorati.com/tag/') for a in links))
        record = topics['javascript']
        body = BeautifulSoup(topic_body(record), 'html.parser')
        self.assertEqual([a['href'] for a in body.select('li a')], [urlsplit(p['link']).path for p in record['posts']])
        self.assertTrue(record['path'].startswith('/topics/'))

    def test_known_permalink_typos_and_redirect_prefix(self):
        for alias, target in ui_repairs()['redirects'].items():
            self.assertEqual(local_url(alias, ORIGIN, {}), target)
            self.assertEqual(local_url(alias.rstrip('/'), ORIGIN, {}), target)
            parser = PrefixHTML('/justaddwater.dk')
            parser.feed('<meta http-equiv="refresh" content="0;url=' + target + '"><a href="' + target + '">Continue</a>')
            soup = BeautifulSoup(''.join(parser.parts), 'html.parser')
            self.assertEqual(soup.meta['content'], '0;url=/justaddwater.dk' + target)
            self.assertEqual(soup.a['href'], '/justaddwater.dk' + target)

    def test_id_links_normalize_percent_encoding_before_route_lookup(self):
        path = '/about/jesper-r%c3%b8nn-jensen/'
        ids = id_routes({'posts': [], 'pages': [], 'media': [{'id': 1, 'link': ORIGIN + path}]})
        expected = '/about/jesper-r%C3%B8nn-jensen/'
        soup = clean_html(parse_document('<a href="/?attachment_id=1">Photo</a>'))
        output = rewrite(soup, ORIGIN, ids, {expected}, set())
        self.assertEqual(output.a['href'], expected)

    def test_podcast_label_becomes_local_download_and_native_audio(self):
        audio = ui_repairs()['audio']
        source = self.posts[audio['post_id']]['content']['rendered']
        soup = clean_html(parse_document(source))
        result = rewrite(soup, ORIGIN, {}, {audio['path']}, set())
        self.assertEqual(result.audio['src'], audio['path'])
        self.assertTrue(result.audio.has_attr('controls'))
        self.assertEqual(result.find('a', string=audio['label'])['href'], audio['path'])
        self.assertTrue(article_text_preserved(source, ' '.join(result.get_text(' ', strip=True).split())))
        blob = (ROOT / 'site' / audio['path'].lstrip('/')).read_bytes()
        self.assertEqual(hashlib.sha256(blob).hexdigest(), audio['sha256'])
        for path in audio['transcripts']:
            soup = clean_html(parse_document('<h3>rails 041 copenhagen</h3><p>Transcript text</p>'), path=path)
            self.assertEqual(soup.audio['src'], audio['path'])
            self.assertIn('Transcript text', soup.get_text())


if __name__ == '__main__':
    unittest.main()
