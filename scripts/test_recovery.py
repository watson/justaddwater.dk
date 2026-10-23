import hashlib
import json
import unittest

from bs4 import BeautifulSoup

from archive import ROOT, ORIGIN, clean_html, parse_document, local_url, rewrite
from prepare_pages import PrefixHTML
from recovery import recovery_data, restore_comments, restore_tag_lists, TABLE_DEMO, BUTTON_DEMO, UNDO_URL, UNDO_PATH
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

    def test_code_examples_preserve_the_original_red_change_highlights(self):
        soup = clean_html(parse_document(self.posts[344]['content']['rendered']))
        expected = {
            'post-344-1': ["echo get_option('siteurl');", 'wp-comments-post.php'],
            'post-344-2': ["bloginfo('template_directory');", 'my-comments-post.php'],
        }
        for key, texts in expected.items():
            block = soup.find(attrs={'data-recovery-code': key})
            self.assertEqual([s.get_text() for s in block.select('span[style="color: #ff0000"]')], texts)
            self.assertIsNone(block.find(['form', 'input', 'script']))
            self.assertEqual(block.get_text(), next(b['code'] for b in recovery_data()['code_blocks'] if b['id'] == key))

    def test_malformed_tag_lists_render_like_simpletags_without_losing_article_text(self):
        for row in recovery_data()['tag_lists']:
            source = self.posts[row['post_id']]['content']['rendered']
            for path in (row['article'], row['article'] + 'comment-page-1/', '/2007/'):
                with self.subTest(post=row['post_id'], path=path):
                    output = clean_html(parse_document(source), path=path)
                    block = output.find(attrs={'data-recovery-tags': str(row['post_id'])})
                    self.assertEqual(block.name, 'small')
                    self.assertEqual(block.parent.name, 'p')
                    self.assertEqual(block.get_text(), 'Technorati Tags: ' + ', '.join(row['tags']))
                    self.assertEqual([a.get_text() for a in block.find_all('a')], row['tags'])
                    self.assertTrue(all(a['rel'] == ['tag'] for a in block.find_all('a')))
                    self.assertNotIn('[tags]', output.get_text())
                    actual = ' '.join(output.get_text(' ', strip=True).split())
                    self.assertTrue(article_text_preserved(source, actual))
                    self.assertFalse(article_text_preserved(source, actual.replace('Technorati Tags:', '')))
                    rendered = str(output)
                    restore_tag_lists(output)
                    self.assertEqual(str(output), rendered)
        undo = clean_html(parse_document(self.posts[718]['content']['rendered']))
        self.assertEqual([a['href'] for a in undo.select('[data-recovery-tags] a')], [
            'http://technorati.com/tag/asa+raskin', 'http://technorati.com/tag/usability',
            'http://technorati.com/tag/undo', 'http://technorati.com/tag/confirmation'])

    def test_existing_tag_lists_and_literal_examples_remain_unchanged(self):
        snippets = [
            '<p><small>Technorati Tags: <a href="http://technorati.com/tag/usability" rel="tag">usability</a></small></p>',
            '<p><code>[tags]asa raskin, usability, undo, confirmation[tags]</code></p>',
            '<p>[tags]unreviewed example[tags]</p>',
        ]
        for source in snippets:
            with self.subTest(source=source):
                before = parse_document(source)
                self.assertEqual(str(clean_html(parse_document(source))), str(before))

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

    def test_css_example_preserves_enabled_control_types_without_a_submission(self):
        source = '<form action="nothing"><input type="submit" name="button1" value="Submit example"><input type="button" id="button2" value="Button example"><button name="button3">Button element</button></form>'
        output = clean_html(parse_document(source), path=BUTTON_DEMO)
        controls = output.select('input, button')
        self.assertEqual([c.get('type') for c in controls], ['submit', 'button', None])
        self.assertEqual([c.get('value', c.get_text()) for c in controls],
                         ['Submit example', 'Button example', 'Button element'])
        self.assertFalse(output.select('form, [disabled], [aria-disabled], .archive-form-notice'))
        self.assertEqual(output.select_one('.archive-local-form')['role'], 'group')
        for path, markup in [('/other.html', source), (BUTTON_DEMO, source.replace('nothing', '/send.php'))]:
            with self.subTest(path=path, markup=markup):
                unrelated = clean_html(parse_document(markup), path=path)
                self.assertTrue(all(c.has_attr('disabled') for c in unrelated.select('input, button')))
                self.assertIsNotNone(unrelated.select_one('.archive-form-notice'))

    def test_undo_done_is_an_enabled_local_button_without_a_submission_notice(self):
        soup = BeautifulSoup((ROOT / 'site' / UNDO_PATH.lstrip('/')).read_text(), 'html.parser')
        self.assertEqual(soup.select_one('#done')['type'], 'button')
        self.assertFalse(soup.select('form, [disabled], [aria-disabled], .archive-form-notice'))
        self.assertEqual(len(soup.select('#todo-list input[type="checkbox"]')), 10)

    def test_only_approved_comments_are_restored_once_on_their_original_pages(self):
        self.assertEqual({c['id'] for c in recovery_data()['comments']}, {27244, 58286})
        source = '<div id="content"><div class="entry">Original content</div><h3 id="respond">Leave a Reply</h3></div>'
        untouched = restore_comments(parse_document(source), '/unrelated/')
        self.assertIsNone(untouched.select_one('.commentlist'))
        for comment in recovery_data()['comments']:
            with self.subTest(comment=comment['id']):
                soup = parse_document(source)
                restore_comments(soup, comment['path'])
                restore_comments(soup, comment['path'])
                soup = clean_html(soup, path=comment['path'])
                soup = rewrite(soup, ORIGIN + comment['path'], {},
                               {'/archive/', '/2006/11/14/world-usability-day-we-dumped-our-archives/', '/'}, set())
                items = soup.select('.commentlist > li')
                self.assertEqual(len(items), 1)
                item = items[0]
                self.assertEqual(item['id'], f'comment-{comment["id"]}')
                self.assertEqual(item.cite.get_text(), comment['author'])
                self.assertEqual(item.p.get_text(), comment['content'])
                self.assertEqual(item.time['datetime'], comment['date'].replace(' ', 'T'))
                self.assertIn(comment['type'], item['class'])
                self.assertEqual(soup.select_one('.entry').get_text(), 'Original content')
                self.assertLess(str(soup).index('commentlist'), str(soup).index('id="respond"'))
                self.assertFalse(any(a['href'].startswith(ORIGIN) for a in item.select('a[href]')))

    def test_recovered_comment_does_not_replace_an_existing_comment_or_require_a_form(self):
        source = '<div id="content"><p>Archive links</p></div>'
        soup = restore_comments(parse_document(source), '/archive/')
        self.assertIsNotNone(soup.find(id='comment-27244'))
        self.assertIsNone(soup.form)
        soup.find(id='comment-27244').p.string = 'Already present in a newer capture'
        restore_comments(soup, '/archive/')
        self.assertEqual(soup.find(id='comment-27244').p.get_text(), 'Already present in a newer capture')


if __name__ == '__main__':
    unittest.main()
