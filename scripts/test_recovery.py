import hashlib
import json
import unittest

from bs4 import BeautifulSoup

from archive import ROOT, ORIGIN, clean_html, parse_document, local_url, rewrite
from prepare_pages import PrefixHTML
from recovery import recovery_data, TABLE_DEMO, UNDO_URL, UNDO_PATH
from verify import article_text_preserved


class RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'data/content.json').read_text())
        cls.posts = {row['id']: row for row in cls.data['posts']}

    def test_every_recovered_snippet_preserves_source_and_surrounding_prose(self):
        for post_id in {b['post_id'] for b in recovery_data()['code_blocks']}:
            row = self.posts[post_id]
            with self.subTest(post=post_id):
                soup = clean_html(parse_document(row['content']['rendered']))
                for block in [b for b in recovery_data()['code_blocks'] if b['post_id'] == post_id]:
                    code = soup.find(attrs={'data-recovery-code': block['id']})
                    self.assertEqual(code.get_text(), block['code'])
                    self.assertIsNone(code.find(['script', 'form', 'style', 'table']))
                self.assertTrue(article_text_preserved(row['content']['rendered'], ' '.join(soup.get_text(' ', strip=True).split())))

    def test_later_css_edits_survive_and_command_punctuation_is_repaired(self):
        corners = clean_html(parse_document(self.posts[550]['content']['rendered']))
        self.assertIn('line-height: 1px;', corners.get_text())
        commands = clean_html(parse_document(self.posts[594]['content']['rendered']))
        self.assertIn('gem install rails --include-dependencies', commands.get_text())
        self.assertNotIn('–include-dependencies', commands.get_text())

    def test_code_containing_page_tags_and_scripts_is_literal_text(self):
        frame = clean_html(parse_document(self.posts[748]['content']['rendered']))
        self.assertIn('<script Language="Javascript">', frame.code.get_text())
        self.assertIsNone(frame.script)
        table = clean_html(parse_document(self.posts[176]['content']['rendered']))
        self.assertIn('<p>I want table row', table.code.get_text())
        self.assertIsNone(table.style)
        self.assertIsNone(table.table)

    def test_gists_are_complete_inert_text_even_after_project_prefixing(self):
        for gist in recovery_data()['gists'].values():
            row = self.posts[gist['post_id']]
            with self.subTest(post=row['id']):
                soup = clean_html(parse_document(row['content']['rendered']))
                parser = PrefixHTML('/justaddwater.dk')
                parser.feed(str(soup)); parser.close()
                output = BeautifulSoup(''.join(parser.parts), 'html.parser')
                for index, file in enumerate(gist['files']):
                    block = output.find(attrs={'data-recovery-code': f'gist-{row["id"]}-{index+1}'})
                    self.assertEqual(block.get_text(), file['code'])
                    self.assertEqual(hashlib.sha256(block.get_text().encode()).hexdigest(), file['sha256'])
                self.assertIsNone(output.script)

    def test_backup_asset_identity_and_old_url_aliases(self):
        for asset in recovery_data()['assets']:
            self.assertEqual(hashlib.sha256((ROOT / asset['file']).read_bytes()).hexdigest(), asset['sha256'])
        for alias, target in recovery_data()['aliases'].items():
            self.assertEqual(local_url(alias, ORIGIN, {}), local_url(target, ORIGIN, {}))

    def test_demo_scripts_are_selected_by_exact_path_and_undo_is_sandboxed(self):
        source = '<html><head></head><body><table class="slimTable"><tr><td>Cell</td></tr></table><script>legacy()</script></body></html>'
        demo = clean_html(parse_document(source), path=TABLE_DEMO)
        self.assertEqual(demo.script['src'], '/archive-assets/demos.js')
        self.assertEqual(demo.script.get_text(), '')
        self.assertIsNone(clean_html(parse_document(source), path='/other.html').script)
        undo = clean_html(parse_document(f'<iframe src="{UNDO_URL}" width="445" height="450"></iframe>'))
        rewritten = rewrite(undo, ORIGIN, {}, {UNDO_PATH}, set())
        self.assertEqual(rewritten.iframe['src'], UNDO_PATH)
        self.assertEqual(rewritten.iframe['sandbox'], 'allow-scripts')


if __name__ == '__main__':
    unittest.main()
