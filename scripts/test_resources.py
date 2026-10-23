import unittest

from bs4 import BeautifulSoup

from archive import ORIGIN, clean_html, parse_document, rewrite
from prepare_pages import PrefixHTML
from resources import css_urls, resource_urls


class ResourceTests(unittest.TestCase):
    def urls(self, markup):
        return [url for tag in BeautifulSoup(markup, 'html.parser').find_all(True)
                for _, url in resource_urls(tag)]

    def test_stylesheet_imports_fonts_and_backgrounds_are_all_checked(self):
        css = '''/* @import "unused.css"; url(unused.png) */
                 @import "layout.css" screen;
                 @import url("colors.css");
                 @font-face { src: url(//fonts.example/font.woff2) }
                 body { background: url(../img/bg.png) }'''
        self.assertCountEqual(css_urls(css), ['layout.css', 'colors.css', '//fonts.example/font.woff2', '../img/bg.png'])

    def test_connections_styles_scripts_media_and_svg_are_resources(self):
        markup = '''<link rel="dns-prefetch" href="//wordpress.example">
                    <link rel="stylesheet" href="https://css.example/theme.css">
                    <link rel="preload" imagesrcset="//img.example/small.png 1x, //img.example/large.png 2x">
                    <script src="https://js.example/run.js"></script>
                    <video poster="//video.example/cover.jpg"><source src="//video.example/movie.mp4"></video>
                    <audio src="/local.mp3"></audio>
                    <svg><image href="//svg.example/image.svg"></image></svg>'''
        self.assertCountEqual(self.urls(markup), ['//wordpress.example', 'https://css.example/theme.css',
                              '//img.example/small.png', '//img.example/large.png', 'https://js.example/run.js',
                              '//video.example/cover.jpg', '//video.example/movie.mp4', '/local.mp3', '//svg.example/image.svg'])

    def test_links_provenance_and_metadata_are_not_automatic_requests(self):
        markup = '''<a href="https://publisher.example/">Source</a>
                    <blockquote cite="https://publisher.example/quote">Quote</blockquote>
                    <link rel="canonical" href="https://original.example/post">
                    <link rel="alternate" href="https://publisher.example/feed">
                    <meta property="og:image" content="https://publisher.example/image.png">
                    <img src="/local.png" data-original-url="https://publisher.example/image.png">'''
        self.assertEqual(self.urls(markup), ['/local.png'])

    def test_automatic_redirects_are_checked(self):
        self.assertEqual(self.urls('<meta http-equiv="refresh" content="0;url=https://example.com/">'), ['https://example.com/'])

    def test_stylesheet_preservation_and_connection_hint_removal_survive_deployment(self):
        url = 'http://castingwords.com/css/search.css'
        path = '/archive-assets/styles/castingwords/search.css'
        source = f'<head><link rel="dns-prefetch" href="//s.w.org"><link rel="preconnect" href="https://old.example"><link rel="stylesheet" media="screen" href="{url}"></head>'
        output = rewrite(clean_html(parse_document(source)), ORIGIN + '/', {}, {path}, set(), {url: {'path': path}})
        parser = PrefixHTML('/justaddwater.dk')
        parser.feed(str(output))
        parser.close()
        soup = BeautifulSoup(''.join(parser.parts), 'html.parser')
        self.assertFalse(soup.select('link[rel~=dns-prefetch], link[rel~=preconnect]'))
        stylesheet = soup.find('link', attrs={'media': 'screen'})
        self.assertEqual(stylesheet['href'], '/justaddwater.dk' + path)
        self.assertEqual(stylesheet['data-original-url'], url)


if __name__ == '__main__':
    unittest.main()
