import hashlib
import html
import json
from pathlib import Path
import tempfile
import unittest

from bs4 import BeautifulSoup

from audit import ROOT, Expectations, audit_outcome, audit_record, canonical, decode, fragment_ids, health, is_html, local_file, merge_browser, render_report, screenshot_coverage, text_changes, visible_text, visual_comparison


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

    def test_comment_repair_accepts_only_exact_recorded_text_and_keeps_neighbours(self):
        policy = self.policy({'comment_repairs': [{'id': 123, 'captured_text': 'Truncated', 'content': 'Truncated text restored'}]})
        original = '<li id="comment-123"><cite>Author</cite><p>Truncated</p></li><p>Neighbour</p>'
        good = original.replace('<p>Truncated</p>', '<p>Truncated text restored</p>')
        before, after, notes = policy.text_pair(original, good)
        self.assertEqual(before, after)
        self.assertIn('restored-comment-text: 123', notes)
        for bad in (good.replace(' restored', ''), good.replace('<p>Neighbour</p>', ''), good.replace('Author', 'Wrong author')):
            before, after, _ = policy.text_pair(original, bad)
            self.assertTrue(text_changes(before, after))
        before, after, _ = policy.text_pair(original.replace('Truncated', 'Later edit'), good)
        self.assertTrue(text_changes(before, after))

    def test_table_article_repair_still_requires_visual_review(self):
        # The exact fragment behind the March 11 screenshot, independently of
        # the converter: accepting its text does not approve its presentation.
        records = json.loads((ROOT / 'data/recovery.json').read_text())['code_blocks']
        block = next(b for b in records if b['id'] == 'post-176-1')
        original = '<div class="entry">' + block['captured'] + '</div>'
        clone = '<div class="entry"><pre><code>' + html.escape(block['code']) + '</code></pre></div>'
        row = self.capture(block['article'], original, clone)
        self.policy({'code_blocks': [block]})
        row = audit_record(row['path'], row['url'], 'pages', self.cache, self.site, Expectations(self.root), '')
        self.assertTrue(any(f['kind'] == 'text' and f['status'] == 'expected' for f in row['findings']))
        changes = [f for f in row['findings'] if f['kind'] == 'article-structure']
        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]['status'], 'review')
        self.assertIn({'element': 'table', 'before': 1, 'after': 0}, changes[0]['changes'])
        self.assertIn({'element': 'pre', 'before': 0, 'after': 1}, changes[0]['changes'])

    def test_small_local_visual_change_is_not_diluted_by_a_long_page(self):
        from PIL import Image, ImageDraw
        (self.root / 'screenshots').mkdir()
        original = Image.new('RGB', (1280, 20000), 'white')
        clone = original.copy()
        ImageDraw.Draw(clone).rectangle((320, 500, 620, 620), fill='black')
        for side, im in [('original', original), ('clone', clone)]:
            im.save(self.root / 'screenshots' / (side + '.png'))
        row = {'id': 'localized', 'findings': [], 'browser': {
            side: {'screenshot': 'screenshots/' + side + '.png', 'height': 20000,
                   'viewport': {'width': 1280, 'height': 900}}
            for side in ('original', 'clone')}}
        visual_comparison(row, self.root)
        self.assertLess(row['visual']['changed_pixel_fraction'], .01)
        self.assertTrue(any(f['kind'] == 'visual' and f['status'] == 'review' for f in row['findings']))

    def test_missing_browser_evidence_is_explicitly_incomplete(self):
        row = self.capture('/post/', '<p>Same</p>', '<p>Same</p>')
        merge_browser([row], self.root)
        self.assertTrue(any(f['kind'] == 'browser-missing' and f['status'] == 'unverified' for f in row['findings']))

    def test_visual_review_prevents_success_even_with_no_unexplained_findings(self):
        row = self.capture('/post/', '<p>Same</p>', '<p>Same</p>')
        row['findings'] = [{'kind': 'visual', 'status': 'review', 'message': 'Rendered pages differ.'},
                           {'kind': 'text', 'status': 'expected', 'message': 'Recorded code repair.'}]
        metadata = {'created_at': 'test', 'inventory_urls': 1, 'selected_urls': 1}
        render_report([row], self.root, metadata)
        self.assertEqual(metadata['outcome']['status'], 'needs-review')
        self.assertEqual(metadata['outcome']['exit_code'], 2)
        report = (self.root / 'index.html').read_text()
        self.assertIn('Visual reviews pending', report)
        self.assertIn('Review required', report)

    def test_partial_and_unverified_reports_cannot_claim_completion(self):
        for partial, findings in [(True, []), (False, [{'kind': 'baseline', 'status': 'unverified', 'message': 'Missing'}])]:
            with self.subTest(partial=partial):
                row = self.capture('/post/', '<p>Same</p>', '<p>Same</p>')
                row['findings'] = findings
                metadata = {'created_at': 'test', 'inventory_urls': 2 if partial else 1, 'selected_urls': 1}
                render_report([row], self.root, metadata)
                self.assertEqual(metadata['outcome']['status'], 'incomplete')
                self.assertEqual(metadata['outcome']['exit_code'], 2)

    def test_audit_exit_codes_distinguish_complete_errors_and_pending_review(self):
        for statuses, expected in [({}, 0), ({'expected': 2, 'fixed': 1}, 0),
                                   ({'unexplained': 1, 'review': 1}, 1),
                                   ({'review': 1}, 2), ({'unverified': 1}, 2)]:
            with self.subTest(statuses=statuses):
                result = audit_outcome({'urls': 1, 'statuses': statuses}, {'inventory_urls': 1})
                self.assertEqual(result['exit_code'], expected)
        self.assertEqual(audit_outcome({'urls': 0, 'statuses': {}}, {})['exit_code'], 2)

    def test_layout_change_is_reviewed_even_when_pixels_are_identical(self):
        from PIL import Image
        row = self.capture('/post/', '<p>Same</p>', '<p>Same</p>')
        (self.root / 'browser').mkdir()
        Image.new('RGB', (1280, 900), 'white').save(self.root / 'same.png')
        (self.root / 'screenshots').mkdir()
        data = {k: row[k] for k in ('source_sha256', 'clone_sha256')}
        for side, height in [('original', 1250), ('clone', 1527)]:
            data[side] = {'screenshot': 'same.png', 'height': 900,
                          'viewport': {'width': 1280, 'height': 900},
                          'geometry': {'.entry': {'height': height}}}
        (self.root / 'browser' / (row['id'] + '.json')).write_text(json.dumps(data))
        merge_browser([row], self.root)
        layout = next(f for f in row['findings'] if f['kind'] == 'layout')
        self.assertEqual(layout['status'], 'review')
        self.assertEqual(layout['changes'][0]['delta'], 277)
        self.assertFalse(any(f['kind'] == 'visual' for f in row['findings']))

    def test_identical_screenshots_and_small_jpeg_noise_do_not_require_visual_review(self):
        from PIL import Image, ImageDraw
        (self.root / 'screenshots').mkdir()
        before = Image.new('RGB', (1280, 900), 'white')
        after = before.copy()
        ImageDraw.Draw(after).rectangle((300, 400, 800, 800), fill=(250, 250, 250))
        for side, im in [('original', before), ('clone', after)]:
            im.save(self.root / (side + '.png'))
        row = {'id': 'noise', 'findings': [], 'browser': {
            side: {'screenshot': side + '.png', 'height': 900, 'viewport': {'width': 1280, 'height': 900}}
            for side in ('original', 'clone')}}
        visual_comparison(row, self.root)
        self.assertEqual(row['findings'], [])

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

    def test_recorded_missing_image_does_not_hide_wrong_targets_or_new_missing_images(self):
        url, path = 'https://old.test/logo.gif', '/archive-assets/missing/logo.gif'
        (self.root / 'data/external-images.json').write_text(json.dumps({url: {'error': '404', 'missing_path': path}}))
        original = f'<img src="{url}" alt="Logo">'
        clone = f'<img src="{path}" alt="Logo" data-original-url="{url}">'
        good = self.capture('/post/', original, clone)
        self.assertEqual(good['expected_missing_images'], [{'url': path, 'original_url': url, 'alt': 'Logo'}])
        self.assertFalse(any(f['status'] == 'unexplained' for f in good['findings']))
        for wrong in [clone.replace(path, path + '?wrong=1'), clone.replace('data-original-url=', 'data-wrong='), clone + '<img src="/newly-lost.png">', clone.replace('<img ', '<script ')+ '</script>']:
            row = self.capture('/post/', original, wrong)
            self.assertTrue(any(f['kind'] == 'local-target' for f in row['findings']), wrong)
        target = self.site / path.lstrip('/')
        target.parent.mkdir(parents=True); target.write_bytes(b'Unexpected replacement')
        row = self.capture('/post/', original, clone)
        self.assertTrue(any(f['kind'] == 'unexpected-image-file' for f in row['findings']))

    def test_browser_reports_known_missing_and_newly_broken_images_separately(self):
        from PIL import Image
        url, path = 'https://old.test/logo.gif', '/archive-assets/missing/logo.gif'
        (self.root / 'data/external-images.json').write_text(json.dumps({url: {'error': '404', 'missing_path': path}}))
        row = self.capture('/post/', f'<img src="{url}" alt="Logo">', f'<img src="{path}" alt="Logo" data-original-url="{url}">')
        row['base_path'] = '/project'
        (self.root / 'browser').mkdir(); (self.root / 'screenshots').mkdir()
        Image.new('RGB', (1280, 900), 'white').save(self.root / 'same.png')
        data = {k: row[k] for k in ('source_sha256', 'clone_sha256')}
        common = {'screenshot': 'same.png', 'height': 900, 'viewport': {'width': 1280, 'height': 900}}
        data['original'] = {**common, 'brokenImages': [{'url': url, 'alt': 'Logo'}]}
        new_failure = {'url': 'http://archive.test/project/newly-lost.png', 'alt': 'New'}
        data['clone'] = {**common, 'brokenImages': [{'url': 'http://archive.test/project' + path, 'alt': 'Logo'}, new_failure]}
        (self.root / 'browser' / (row['id'] + '.json')).write_text(json.dumps(data))
        merge_browser([row], self.root)
        known = next(f for f in row['findings'] if f['kind'] == 'browser-knownMissingImages')
        other = next(f for f in row['findings'] if f['kind'] == 'browser-brokenImages')
        self.assertEqual(known['status'], 'inherited')
        self.assertEqual(other['status'], 'unexplained')
        self.assertEqual(other['after'], [new_failure])

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

    def test_screenshot_must_cover_full_page_up_to_explicit_cap(self):
        info = {'height': 3400, 'viewport': {'width': 1280, 'height': 900}}
        self.assertEqual(screenshot_coverage(info, 1280, 900), {'expected': [1280, 3400], 'actual': [1280, 900]})
        self.assertIsNone(screenshot_coverage(info, 1280, 3400))
        self.assertIsNone(screenshot_coverage({**info, 'height': 60000}, 1280, 50000))

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

    def test_preserved_stylesheet_mapping_does_not_approve_unrecorded_replacement(self):
        url = 'https://old.test/theme.css'
        (self.root / 'data/external-resources.json').write_text(json.dumps({'resources': {
            url: {'path': '/archive-assets/theme.css', 'kind': 'stylesheet'}}}))
        policy = self.policy()
        old = [{'tag': 'link', 'attribute': 'href', 'url': url, 'label': ''}]
        for path, expected in [('/archive-assets/theme.css', []), ('/wrong.css', old)]:
            new = [{'tag': 'link', 'attribute': 'href', 'url': path, 'label': ''}]
            problems, _ = policy.reference_issues(old, new, '/')
            self.assertEqual(problems, expected)

    def test_editorial_code_highlighting_does_not_change_literal_text(self):
        original = BeautifulSoup('<pre>&lt;form action="/file.php"&gt;</pre>', 'html.parser')
        actual = BeautifulSoup('<pre><code>&lt;form action="/<span style="color: #ff0000">file.php</span>"&gt;</code></pre>', 'html.parser')
        self.assertEqual(visible_text(original), visible_text(actual))
        actual.span.string = 'wrong.php'
        self.assertNotEqual(visible_text(original), visible_text(actual))

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

    def test_retired_dependency_exception_only_matches_the_recorded_url(self):
        (self.root / 'data/audit-repairs.json').write_text(json.dumps({
            'unavailable_references': {'https://old.test/widget.js': {'replacement': None, 'reason': 'Retired widget'}}}))
        policy = self.policy()
        old = [{'tag': 'script', 'attribute': 'src', 'url': url, 'label': ''}
               for url in ('https://old.test/widget.js', 'https://old.test/demo.js')]
        new = [{'tag': 'script', 'attribute': 'src', 'url': '/archive-assets/archive.js', 'label': ''}]
        unexplained, explained = policy.reference_issues(old, new, '/')
        self.assertEqual(unexplained, [old[1]])
        self.assertEqual(explained[0]['reference'], old[0])

    def test_repaired_excerpt_does_not_hide_unrelated_text_loss(self):
        (self.root / 'data/audit-repairs.json').write_text(json.dumps({'excerpts': [
            {'post_id': 1, 'captured_text': '[code]Example', 'text': 'Example'}]}))
        original = '<div class="entry"><p>[code]Example</p><p>Keep this sentence.</p></div>'
        clone = '<div class="entry"><p>Example</p></div>'
        before, after, notes = self.policy().text_pair(original, clone)
        self.assertNotEqual(before, after)
        self.assertIn('Keep this sentence.', before)
        self.assertIn('excerpt: 1', notes)


if __name__ == '__main__':
    unittest.main()
