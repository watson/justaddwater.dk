import hashlib
import json
from pathlib import Path
import unittest

from bs4 import BeautifulSoup

from archive import ORIGIN, ROOT, clean_html, local_url, parse_document, rewrite
from reconcile import decode_document, repairs


class ReconciliationTests(unittest.TestCase):
    def test_response_links_and_closed_comment_targets_resolve(self):
        soup = clean_html(parse_document('<a href="#respond">Reply</a><h3 id="respond">Leave a reply</h3><form id="commentform"><input></form>'))
        self.assertEqual(soup.a['href'], '#respond')
        self.assertIsNotNone(soup.find(id='respond'))
        self.assertIsNotNone(soup.find(id='comments'))
        closed = clean_html(parse_document('<p class="nocomments">Comments are closed.</p>'))
        self.assertEqual(closed.p['id'], 'comments')

    def test_duplicate_forms_keep_styles_labels_and_inert_controls(self):
        fragment = '<h3 id="respond">Reply</h3><form id="commentform"><label for="author">Name</label><input id="author"><input id="submit" type="submit"></form>'
        soup = clean_html(parse_document('<style>#page {background:url(bg.jpg)}</style>' + fragment * 2))
        ids = [t['id'] for t in soup.select('[id]')]
        self.assertEqual(len(ids), len(set(ids)))
        for group in soup.select('.archive-form'):
            self.assertIn('archive-commentform', group['class'])
            self.assertIsNotNone(group.find(id=group.label['for']))
            self.assertTrue(all(t.has_attr('disabled') for t in group.select('input')))
        self.assertIn('url(bg.jpg)', soup.style.string)

    def test_search_query_and_feed_scope_survive_rewriting(self):
        source = '<a href="/?s=innovation%20test">Search</a><a href="http://feeds.justaddwater.dk/jaw/comments">Comments</a><a href="/feed/?attachment_id=42">Attachment feed</a>'
        soup = rewrite(clean_html(parse_document(source)), ORIGIN + '/', {'42': '/photo/'}, {'/photo/feed/'}, set())
        self.assertEqual([a['href'] for a in soup.find_all('a')], ['/archive-search/?s=innovation%20test', '/comments/feed/', '/photo/feed/'])

    def test_utf8_bytes_override_obsolete_meta_without_corrupting_names(self):
        raw = '<meta charset="iso-8859-1"><p>Jesper Rønn-Jensen</p>'.encode()
        soup = clean_html(parse_document(raw))
        self.assertEqual(soup.p.text, 'Jesper Rønn-Jensen')
        self.assertEqual(soup.meta['charset'], 'utf-8')

    def test_first_pagination_page_is_the_homepage(self):
        for query in ('page=0', 'page=1', 'paged=1'):
            self.assertEqual(local_url('/?' + query, ORIGIN, {}), '/')
        for query in ('page=2', 'paged=02'):
            self.assertEqual(local_url('/?' + query, ORIGIN, {}), '/page/2/')

    def test_intact_backup_recovers_transfer_damage_and_rejects_drift(self):
        for path, record in repairs()['html_sources'].items():
            if not record.get('file'):
                continue
            backup = (ROOT / record['file']).read_bytes()
            damaged = backup.replace(b'\r', b'')
            self.assertEqual(hashlib.sha256(damaged).hexdigest(), record['capture_sha256'])
            text = decode_document(damaged, path)
            self.assertIn('<html>', text)
            self.assertNotIn('\ufffd', text)
            soup = clean_html(parse_document(damaged, path), path)
            if 'cookieeditor' in path:
                self.assertEqual(soup.body.get_text(' ', strip=True), 'CookEd')
                self.assertIsNotNone(soup.select_one('a[data-archive-bookmarklet]'))
            with self.assertRaises(ValueError):
                decode_document(damaged + b'changed', path)

    def test_conditional_comment_example_is_visible_without_execution(self):
        source = '<p>Conditional stylesheet (' + repairs()['literal_fragments'][0]['captured'] + ')</p>'
        soup = clean_html(parse_document(source))
        self.assertEqual(soup.code.text, '<!--[if IE]><![endif]-->')
        self.assertIn('Conditional stylesheet', soup.p.text)

    def test_excerpt_repairs_do_not_change_other_paragraphs(self):
        for record in repairs()['excerpts']:
            source = '<div class="entry"><p>' + record['captured_text'] + '</p><p>Keep this prose.</p></div>'
            soup = clean_html(parse_document(source))
            self.assertEqual(soup.p.text, record['text'])
            self.assertEqual(soup.find_all('p')[1].text, 'Keep this prose.')


if __name__ == '__main__':
    unittest.main()
