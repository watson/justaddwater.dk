import json
import unittest

from bs4 import BeautifulSoup

from archive import ROOT, ORIGIN, REPAIRED_CODE_ARTICLE, clean_html, parse_document, references, rewrite
from prepare_pages import PrefixHTML
from verify import article_text_preserved, video_embed_markup


class BackgroundCaptureTests(unittest.TestCase):
    def test_theme_background_is_discovered_and_survives_project_deployment(self):
        path = '/wp-content/themes/jaw/images/kubrickbg-ltr.jpg'
        source = f'<html><head><style>#page {{ background: url("{ORIGIN}{path}") repeat-y top; border: none; }}</style></head><body></body></html>'
        soup = parse_document(source)
        _, assets = references(soup, ORIGIN + '/', {})
        self.assertIn(path, assets)
        output = rewrite(soup, ORIGIN + '/', {}, {path}, set())
        parser = PrefixHTML('/justaddwater.dk')
        parser.feed(str(output))
        parser.close()
        deployed = BeautifulSoup(''.join(parser.parts), 'html.parser')
        self.assertEqual(deployed.style.string,
                         f'#page {{ background: url("/justaddwater.dk{path}") repeat-y top; border: none; }}')

    def test_embedded_demo_backgrounds_resolve_relative_to_the_document(self):
        soup = parse_document('<style>.tip {background:url(train-done.png)}</style><p style="background:url(../bullet.png)"></p>')
        base = ORIGIN + '/wp-content/uploads/2007/10/demo.html'
        paths = {'/wp-content/uploads/2007/10/train-done.png', '/wp-content/uploads/2007/bullet.png'}
        self.assertEqual(references(soup, base, {})[1], paths)
        output = rewrite(soup, base, {}, paths, set())
        self.assertIn('url("/wp-content/uploads/2007/10/train-done.png")', output.style.string)
        self.assertEqual(output.p['style'], 'background:url("/wp-content/uploads/2007/bullet.png")')

    def test_external_background_uses_captured_image(self):
        url = 'http://example.com/background.png'
        soup = parse_document(f'<style>button {{background: url({url})}}</style>')
        output = rewrite(soup, ORIGIN + '/', {}, set(), set(),
                         {url: {'path': '/archive-assets/external/background.png'}})
        self.assertIn('url("/archive-assets/external/background.png")', output.style.string)


class LegacyMarkupTests(unittest.TestCase):
    def test_downloadable_demo_controls_remain_visible_without_submission(self):
        source = '<form action="/send.php" method="post"><input type="submit" value="CSS example"><button onclick="submit()">Example</button></form>'
        demo = clean_html(parse_document(source), preserve_demo_controls=True)
        self.assertIsNone(demo.form)
        self.assertEqual(demo.input['value'], 'CSS example')
        self.assertEqual(demo.button.get_text(), 'Example')
        self.assertNotIn('onclick', demo.button.attrs)
        self.assertNotIn('action', demo.div.attrs)
        self.assertIsNone(clean_html(parse_document(source)).input)

    def test_browser_formatting_survives_code_tag_crossing_paragraphs(self):
        # WordPress emitted this structure in the 2016 Git extraction article.
        source = '<p><code>ORIG=source<br>DEST=target</p><p>git clone $ORIG $DEST</code></p><p>A few notes:</p>'
        output = clean_html(parse_document(source))
        paragraphs = output.find_all('p')
        self.assertEqual(paragraphs[1].code.get_text(), 'git clone $ORIG $DEST')
        self.assertIsNone(paragraphs[2].code)
        self.assertEqual(parse_document(str(output)).body, output.body)

    def test_unclosed_table_can_move_article_text_around_template_text(self):
        article = '<p>Before table</p><table><tr><td>Cell text</td></tr><p>After table</p>'
        document = parse_document(article + '<footer>Template footer</footer>')
        actual = ' '.join(document.get_text(' ', strip=True).split())
        self.assertTrue(article_text_preserved(article, actual))
        self.assertFalse(article_text_preserved(article, actual.replace('Cell text', '')))
        self.assertFalse(article_text_preserved(article, actual.replace('After table', '')))


class FormExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / 'data/content.json').read_text())
        cls.article = next(row['content']['rendered'] for row in data['posts']
                           if row['slug'] == 'blog-usability-avoid-spam-comments')

    def test_original_article_keeps_example_and_every_section_after_it(self):
        output = clean_html(parse_document(self.article))
        text = output.get_text(' ', strip=True)
        self.assertIn('<form id="postform" method="post" action="illegal.url">', text)
        for section in ('Moderate all comments before publishing', 'What we won’t do',
                        'Captcha', 'More info:', 'WordPress comment spam stoppage techniques'):
            self.assertIn(section, text)
        self.assertIsNone(output.find('form', id='postform'))
        self.assertNotIn('This form no longer accepts submissions.', text)
        self.assertTrue(article_text_preserved(self.article, ' '.join(text.split())))

    def test_validator_rejects_the_previous_loss_instead_of_repeating_it(self):
        broken = BeautifulSoup(self.article, 'html.parser')
        broken.form.replace_with('This form no longer accepts submissions.')
        actual = ' '.join(broken.get_text(' ', strip=True).split())
        self.assertFalse(article_text_preserved(self.article, actual))

    def test_byte_capture_preserves_unicode_and_literal_form_tags(self):
        source = '<meta charset="utf-8"><p>[code lang="html"]<form action="example?a=1&amp;b=2">Example</form>[/code]</p><p>François’ notes</p>'
        for raw in (source, source.encode('utf-8')):
            output = clean_html(parse_document(raw))
            text = output.get_text(' ', strip=True)
            self.assertIn('<form action="example?a=1&amp;b=2">Example</form>', text)
            self.assertIn('François’ notes', text)
            self.assertIsNone(output.form)

    def test_repaired_article_has_separate_code_blocks_and_following_paragraph(self):
        for path in (REPAIRED_CODE_ARTICLE, REPAIRED_CODE_ARTICLE + 'comment-page-1/'):
            for raw in (self.article, self.article.encode('utf-8')):
                with self.subTest(path=path, binary=isinstance(raw, bytes)):
                    output = clean_html(parse_document(raw, path=path))
                    blocks = output.select('pre.archive-code > code')
                    self.assertEqual(len(blocks), 2)
                    self.assertEqual(blocks[0]['class'], ['language-html'])
                    self.assertEqual(blocks[0].get_text(), '<form id="postform" method="post" action="illegal.url">')
                    self.assertEqual(blocks[1]['class'], ['language-javascript'])
                    self.assertEqual(blocks[1].get_text(),
                                     'var obj = document.getElementById(‘postform’)\nif(obj)\nobj.action = “wp-comments-post.php”')
                    following = blocks[0].parent.find_next_sibling()
                    self.assertEqual(following.name, 'p')
                    self.assertTrue(following.get_text().startswith('And then via DOM scripting'))
                    self.assertIsNone(output.find('form', id='postform'))
                    text = ' '.join(output.get_text(' ', strip=True).split())
                    self.assertNotIn('[code', text)
                    self.assertNotIn('[/code]', text)
                    self.assertTrue(article_text_preserved(self.article, text, rendered_code=True))
                    for missing in ('<form id="postform" method="post" action="illegal.url">',
                                    'obj.action = “wp-comments-post.php”', 'Captcha'):
                        damaged = ' '.join(text.replace(missing, '').split())
                        self.assertFalse(article_text_preserved(self.article, damaged, rendered_code=True))

    def test_other_articles_keep_their_existing_code_presentation(self):
        output = parse_document(self.article, path='/another-article/')
        self.assertFalse(output.select('pre.archive-code'))
        self.assertIn('[code', output.get_text())


class VideoEmbedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / 'data/content.json').read_text())
        # These two articles contain an interactive demo and literal object-tag
        # examples, respectively. All other embedded players are videos.
        excluded = {'undo-not-confirmation-end-of-discussion', 'ie-7-web-standards-and-css-support'}
        cls.articles = [row for row in data['posts'] if row['slug'] not in excluded
                        and BeautifulSoup(row['content']['rendered'], 'html.parser').find(['iframe', 'object', 'embed'])]

    def test_all_original_players_survive_conversion_and_project_deployment(self):
        self.assertEqual(len(self.articles), 21)
        for row in self.articles:
            with self.subTest(article=row['slug']):
                original = BeautifulSoup(row['content']['rendered'], 'html.parser')
                expected = [str(tag) for tag in original.find_all(['iframe', 'object', 'embed'])]
                output = rewrite(clean_html(parse_document(row['content']['rendered'])),
                                 row['link'], {}, set(), set())
                parser = PrefixHTML('/justaddwater.dk')
                parser.feed(str(output))
                parser.close()
                deployed = BeautifulSoup(''.join(parser.parts), 'html.parser')
                actual = [str(tag) for tag in deployed.find_all(['iframe', 'object', 'embed'])]
                self.assertEqual(actual, expected)

    def test_video_check_detects_removed_players_and_changed_parameters(self):
        article = next(row for row in self.articles if row['slug'] == 'lessons-learned-from-pixar-2')
        source = article['content']['rendered']
        expected = video_embed_markup(BeautifulSoup(source, 'html.parser'))
        for mutation in ('remove', 'url', 'dimensions', 'parameter'):
            with self.subTest(mutation=mutation):
                output = clean_html(parse_document(source))
                self.assertEqual(video_embed_markup(output), expected)
                if mutation == 'remove':
                    output.object.decompose()
                elif mutation == 'url':
                    output.embed['src'] = 'http://www.youtube.com/v/changed'
                elif mutation == 'dimensions':
                    output.object['width'] = '1'
                else:
                    output.find('param', attrs={'name': 'movie'})['value'] = 'http://www.youtube.com/v/changed'
                self.assertNotEqual(video_embed_markup(output), expected)

    def test_unrelated_embeds_and_scripts_are_still_removed(self):
        source = '<iframe src="http://humanized.com/demo.html"></iframe><object data="example.swf"><embed src="example.swf"></object><applet></applet><script>tracking()</script>'
        output = clean_html(parse_document(source))
        self.assertIsNone(output.find(['iframe', 'object', 'embed', 'applet', 'script']))


if __name__ == '__main__':
    unittest.main()
