import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from bs4 import BeautifulSoup

from audit import Expectations, audit_record, canonical, decode, fragment_ids, health, is_html, local_file, text_changes


class AuditTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'data').mkdir()
        self.cache = self.root / 'cache'
        self.site = self.root / 'site'
        self.cache.mkdir()
        self.site.mkdir()

    def policy(self, recovery=None):
        (self.root / 'data/recovery.json').write_text(json.dumps(recovery or {}))
        return Expectations(self.root)

    def capture(self, path, original, clone):
        url = 'http://justaddwater.dk' + path
        stem = self.cache / hashlib.sha256(url.encode()).hexdigest()
        stem.with_suffix('.body').write_text(original)
        stem.with_suffix('.json').write_text(json.dumps({'url': url, 'status': 200, 'headers': {'Content-Type': 'text/html; charset=utf-8'}}))
        target = self.site / path.lstrip('/') / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(clone)
        return audit_record(path, url, 'pages', self.cache, self.site, self.policy(), '')

    def test_expected_repair_does_not_hide_deleted_neighbouring_prose(self):
        policy = self.policy({'code_blocks': [{'id': 'one', 'captured': '[code]<form action="bad">[/code]', 'code': '<form action="bad">'}]})
        original = '<p>Before</p>[code]<form action="bad">[/code]<p>Do not lose this paragraph.</p>'
        good = '<p>Before</p><pre>&lt;form action="bad"&gt;</pre><p>Do not lose this paragraph.</p>'
        before, after, notes = policy.text_pair(original, good)
        self.assertEqual(before, after)
        before, after, _ = policy.text_pair(original, good.replace('<p>Do not lose this paragraph.</p>', ''))
        self.assertTrue(text_changes(before, after))
        self.assertIn('code: one', notes)

    def test_inherited_bug_is_reported_even_when_pages_match(self):
        row = self.capture('/post/', '<p>[tags]broken[tags]</p>', '<p>[tags]broken[tags]</p>')
        self.assertTrue(any(f['kind'] == 'shortcode' and f['status'] == 'inherited' for f in row['findings']))

    def test_changed_remote_link_is_not_silently_ignored(self):
        row = self.capture('/post/', '<a href="https://example.org/right">Article</a>', '<a href="https://example.org/wrong">Article</a>')
        self.assertTrue(any(f['kind'] == 'changed-reference' for f in row['findings']))

    def test_removed_demo_scripts_need_review(self):
        row = self.capture('/demo/', '<script>window.demo = function() {};</script><script src="/demo.js"></script>', '<p>Example</p>')
        self.assertTrue({'inline-behavior', 'changed-reference'} <= {f['kind'] for f in row['findings']})

    def test_swapped_link_targets_are_not_hidden_by_identical_url_sets(self):
        row = self.capture('/post/', '<a href="https://example.org/a">One</a><a href="https://example.org/b">Two</a>',
                           '<a href="https://example.org/b">One</a><a href="https://example.org/a">Two</a>')
        self.assertTrue(any(f['kind'] == 'link-label-target' for f in row['findings']))

    def test_missing_image_and_comment_are_reported(self):
        row = self.capture('/post/', '<ul><li id="comment-1">Hello</li></ul>', '<img src="/missing.png">')
        self.assertTrue({'local-target', 'missing-comment', 'text'} <= {f['kind'] for f in row['findings']})

    def test_url_normalization_preserves_semantic_query_and_fragment(self):
        self.assertEqual(canonical('https://watson.github.io/justaddwater.dk/a%20b/?p=4#reply'), '/a b/?p=4#reply')
        self.assertEqual(canonical('/file.css?ver=1'), '/file.css')
        self.assertEqual(canonical('/file.css?important=1'), '/file.css?important=1')

    def test_paths_resolve_feeds_percent_encoding_and_block_traversal(self):
        (self.site / 'feed').mkdir()
        (self.site / 'feed/index.xml').write_text('<rss/>')
        (self.site / 'a b.txt').write_text('x')
        self.assertEqual(local_file(self.site, '/feed/').name, 'index.xml')
        self.assertEqual(local_file(self.site, '/a%20b.txt').name, 'a b.txt')
        self.assertIsNone(local_file(self.site, '/%2e%2e/private.txt'))

    def test_enabled_archived_controls_detected(self):
        result = health(BeautifulSoup('<div class="archive-form"><input></div>', 'html.parser'))
        self.assertIn('enabled-archived-form', result)

    def test_bom_and_legacy_meta_encodings(self):
        value = '<html><body>Rønn-Jensen</body></html>'
        self.assertEqual(decode(value.encode('utf-16')), value)
        self.assertEqual(decode(value.encode('utf-8-sig')), value)
        latin = '<meta charset="windows-1252"><p>Rønn-Jensen</p>'
        self.assertEqual(decode(latin.encode('cp1252')), latin)

    def test_fragment_target_and_unexpected_form(self):
        row = self.capture('/post/', '<p id="here">Hello</p>', '<a href="#gone">Go</a><form action="/submit" method="post"><input></form>')
        self.assertTrue({'fragment-target', 'active-submission'} <= {f['kind'] for f in row['findings']})

    def test_missing_baseline_is_not_a_pass(self):
        row = audit_record('/missing/', 'http://justaddwater.dk/missing/', 'pages', self.cache, self.site, self.policy(), '')
        self.assertEqual(row['findings'][0]['status'], 'unverified')

    def test_javascript_with_wrong_server_mime_is_a_download(self):
        self.assertFalse(is_html(b'function example() {}', 'text/html', '/example.js'))

    def test_recorded_alias_matches_existing_target_not_only_added_links(self):
        policy = self.policy({'aliases': {'/old.ppt': '/new.ppt'}})
        old = [{'tag': 'a', 'attribute': 'href', 'url': '/old.ppt', 'label': 'Slides'}]
        new = [{'tag': 'a', 'attribute': 'href', 'url': '/new.ppt', 'label': 'Slides'}]
        unexplained, explained = policy.reference_issues(old, new, '/')
        self.assertEqual(unexplained, [])
        self.assertEqual(len(explained), 1)

    def test_literal_code_is_not_a_fragment_target(self):
        file = self.site / 'page.html'
        file.write_text('<code>&lt;div id="example"&gt;</code><a name="actual"></a>')
        self.assertEqual(fragment_ids(file), {'actual'})

    def test_capture_inventory_redirect_retains_requested_url(self):
        target = 'http://justaddwater.dk/canonical/'
        stem = self.cache / hashlib.sha256(target.encode()).hexdigest()
        stem.with_suffix('.body').write_text('<html><p>Original</p></html>')
        stem.with_suffix('.json').write_text(json.dumps({'url': target, 'final_url': target, 'status': 200}))
        (self.cache / 'capture.json').write_text(json.dumps({'pages': {'/alias/': target}}))
        policy = Expectations(self.root, self.cache)
        self.assertEqual(policy.capture_aliases['/alias/'], '/canonical/')
        row = audit_record('/alias/', target, 'pages', self.cache, self.site, policy, '')
        self.assertEqual(row['url'], 'http://justaddwater.dk/alias/')
        self.assertEqual(row['capture_url'], target)

    def test_expected_footer_must_match_exactly(self):
        original = '<div id="footer"><p>Privacy Policy justaddwater.dk is proudly powered by WordPress</p></div>'
        modified = '<div id="footer"><p>Privacy Policy justaddwater.dk was proudly powered by WordPress. Unexpected</p></div>'
        a, b, notes = self.policy().text_pair(original, modified)
        self.assertNotEqual(a, b)
        self.assertNotIn('archive-footer', notes)


if __name__ == '__main__':
    unittest.main()
