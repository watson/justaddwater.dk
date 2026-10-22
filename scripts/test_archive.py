import unittest

from bs4 import BeautifulSoup

from archive import ORIGIN, clean_html, parse_document, references, rewrite
from prepare_pages import PrefixHTML
from verify import article_text_preserved


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


if __name__ == '__main__':
    unittest.main()
