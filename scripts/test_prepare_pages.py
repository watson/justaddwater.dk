import unittest

from prepare_pages import PrefixHTML


class ProjectPrefixTests(unittest.TestCase):
    def rewrite(self, source):
        parser = PrefixHTML('/justaddwater.dk')
        parser.feed(source)
        parser.close()
        return ''.join(parser.parts)

    def test_real_links_change_but_published_code_examples_do_not(self):
        source = '<a href="/archive/">Archive</a><pre>&lt;link href="/example.css"&gt;</pre>'
        self.assertEqual(self.rewrite(source),
                         '<a href="/justaddwater.dk/archive/">Archive</a><pre>&lt;link href="/example.css"&gt;</pre>')

    def test_external_and_protocol_relative_links_are_preserved(self):
        source = '<a href="https://example.com/a">a</a><img src="//example.com/a.png"/>'
        self.assertEqual(self.rewrite(source), source)

    def test_image_variants_and_inline_backgrounds_use_project_prefix(self):
        source = '<img src="/a.png" srcset="/a.png 1x, /b.png 2x" style="background:url(/c.png)"/>'
        output = self.rewrite(source)
        for name in ('a.png', 'b.png', 'c.png'):
            self.assertIn('/justaddwater.dk/' + name, output)


if __name__ == '__main__':
    unittest.main()
