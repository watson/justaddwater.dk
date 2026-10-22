import json
import re
import unittest
from urllib.parse import parse_qs, urlsplit

from bs4 import BeautifulSoup

from archive import ROOT, ORIGIN, clean_html, parse_document, references, rewrite
from prepare_pages import PrefixHTML
from verify import archived_form_errors, article_text_preserved, video_embed_markup, expected_video_markup
from recovery import video_players


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
        demo = clean_html(parse_document(source))
        self.assertIsNone(demo.form)
        self.assertEqual(demo.input['value'], 'CSS example')
        self.assertEqual(demo.button.get_text(), 'Example')
        self.assertNotIn('onclick', demo.button.attrs)
        self.assertNotIn('action', demo.div.attrs)
        self.assertTrue(demo.input.has_attr('disabled'))
        self.assertTrue(demo.button.has_attr('disabled'))

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


class ArchivedFormTests(unittest.TestCase):
    def test_contact_form_keeps_its_labels_and_controls_but_cannot_submit(self):
        data = json.loads((ROOT / 'data/content.json').read_text())
        source = next(row['content']['rendered'] for row in data['pages'] if row['slug'] == 'contact-us')
        output = clean_html(parse_document(source))
        controls = output.select('input, textarea, button, select')
        self.assertEqual([control.get('name') for control in controls],
                         ['wpcf_your_name', 'wpcf_email', 'wpcf_website', 'wpcf_msg', 'Submit'])
        self.assertTrue(all(control.has_attr('disabled') for control in controls))
        self.assertIsNone(output.form)
        group = output.select_one('.archive-form')
        self.assertNotIn('action', group.attrs)
        self.assertEqual(group['aria-disabled'], 'true')
        self.assertEqual(group.textarea['rows'], '8')
        self.assertEqual(group.textarea['cols'], '35')
        self.assertEqual(len(group.find_all('label')), 4)
        notice = output.find(id=group['aria-describedby'])
        self.assertIn('This form no longer accepts submissions.', notice.get_text())
        self.assertIn('archive-form-notice', notice['class'])

    def test_comment_form_is_visible_but_disabled_without_runtime_fields(self):
        source = '<h3 id="respond">Leave a Reply</h3><form id="commentform" action="/wp-comments-post.php" method="post"><textarea name="comment" autofocus tabindex="1"></textarea><input type="submit" value="Submit Comment" formaction="/other.php"><input type="hidden" name="nonce" value="runtime"><p style="display: none !important;"><input name="honeypot" value="runtime"></p></form>'
        output = clean_html(parse_document(source))
        self.assertIsNotNone(output.find(id='respond'))
        self.assertIsNotNone(output.find(id='commentform'))
        self.assertTrue(output.textarea.has_attr('disabled'))
        self.assertTrue(output.input.has_attr('disabled'))
        self.assertFalse(output.select('[autofocus], [tabindex], [formaction], [type="hidden"], [name="honeypot"]'))
        self.assertIsNone(output.form)

    def test_archive_search_stays_usable_next_to_a_disabled_form(self):
        source = '<form id="searchform" action="/"><input name="s"><input type="submit" value="Search"></form><form action="/send"><input name="message"><button>Send</button></form>'
        output = clean_html(parse_document(source))
        self.assertEqual(output.form['action'], '/search/')
        self.assertEqual(output.form['method'], 'get')
        self.assertFalse(output.form.select('[disabled]'))
        self.assertEqual(len(output.select('.archive-form-notice')), 1)
        self.assertTrue(output.button.has_attr('disabled'))

    def test_validator_rejects_enabled_controls_and_missing_notices(self):
        source = '<form action="/send"><input name="message"><button>Send</button></form>'
        for mutation in ('enabled', 'notice', 'endpoint', 'association'):
            with self.subTest(mutation=mutation):
                output = clean_html(parse_document(source))
                self.assertEqual(archived_form_errors(output), [])
                if mutation == 'enabled':
                    del output.input['disabled']
                elif mutation == 'notice':
                    output.select_one('.archive-form-notice').decompose()
                elif mutation == 'endpoint':
                    output.select_one('.archive-form')['action'] = '/send'
                else:
                    output.button['form'] = 'searchform'
                self.assertTrue(archived_form_errors(output))


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
        REPAIRED_CODE_ARTICLE = '/2006/06/24/blog-usability-avoid-spam-comments/'
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
                                     "var obj = document.getElementById('postform')\n\nif(obj)\n\nobj.action = \"wp-comments-post.php\"")
                    following = blocks[0].parent.find_next_sibling()
                    self.assertEqual(following.name, 'p')
                    self.assertTrue(following.get_text().startswith('And then via DOM scripting'))
                    self.assertIsNone(output.find('form', id='postform'))
                    text = ' '.join(output.get_text(' ', strip=True).split())
                    self.assertNotIn('[code', text)
                    self.assertNotIn('[/code]', text)
                    self.assertTrue(article_text_preserved(self.article, text))
                    for missing in ('<form id="postform" method="post" action="illegal.url">',
                                    'obj.action = "wp-comments-post.php"', 'Captcha'):
                        damaged = ' '.join(text.replace(missing, '').split())
                        self.assertFalse(article_text_preserved(self.article, damaged))

    def test_repaired_examples_also_work_in_archive_listing_pages(self):
        output = parse_document(self.article, path='/2006/06/')
        self.assertEqual(len(output.select('pre.archive-code')), 2)
        self.assertNotIn('[code', output.get_text())


class VideoEmbedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / 'data/content.json').read_text())
        # These two articles contain an interactive demo and literal object-tag
        # examples, respectively. All other embedded players are videos.
        excluded = {'undo-not-confirmation-end-of-discussion', 'ie-7-web-standards-and-css-support'}
        cls.articles = [row for row in data['posts'] if row['slug'] not in excluded
                        and BeautifulSoup(row['content']['rendered'], 'html.parser').find(['iframe', 'object', 'embed'])]

    def test_all_recorded_players_survive_conversion_and_project_deployment(self):
        self.assertEqual(len(self.articles), 21)
        for row in self.articles:
            with self.subTest(article=row['slug']):
                expected = expected_video_markup(row)
                output = rewrite(clean_html(parse_document(row['content']['rendered'])),
                                 row['link'], {}, set(), set())
                parser = PrefixHTML('/justaddwater.dk')
                parser.feed(str(output))
                parser.close()
                deployed = BeautifulSoup(''.join(parser.parts), 'html.parser')
                actual = video_embed_markup(deployed)
                self.assertEqual(actual, expected)

    def test_native_players_preserve_original_ids_sizes_and_supported_options(self):
        migrated = set()
        for row in self.articles:
            if row['id'] in (805, 1168, 1378):  # Owner approved different uploads.
                continue
            original = BeautifulSoup(row['content']['rendered'], 'html.parser').find(['object', 'iframe', 'embed'])
            movie = original.find('param', attrs={'name': 'movie'})
            source = movie['value'] if movie else original.get('src', '')
            if not (source.startswith('http://www.youtube.com/v/') or 'player.vimeo.com' in source):
                continue
            with self.subTest(article=row['slug']):
                record = next(item for item in video_players() if item['post_id'] == row['id'])
                self.assertEqual(record['captured'], str(original))
                # Check the actual conversion against the original API data,
                # independently of the recorded replacement HTML.
                output = clean_html(parse_document(row['content']['rendered']))
                self.assertEqual(len(output.find_all(['object', 'iframe', 'embed'])), 1)
                frame = output.iframe
                self.assertEqual((frame['width'], frame['height']), (original['width'], original['height']))
                if 'youtube.com' in source:
                    video_id, _, query = source.split('/v/')[1].partition('&')
                    self.assertEqual(urlsplit(frame['src']).path, '/embed/' + video_id)
                    options = {k: v for k, v in parse_qs(query).items() if k in ('hl', 'fs', 'rel')}
                    self.assertEqual(parse_qs(urlsplit(frame['src']).query), options)
                    self.assertEqual(urlsplit(frame['src']).hostname, 'www.youtube.com')
                else:
                    self.assertEqual(frame['src'], source.replace('http:', 'https:', 1))
                self.assertEqual(urlsplit(frame['src']).scheme, 'https')
                self.assertTrue(frame.has_attr('allowfullscreen'))
                self.assertEqual(frame['frameborder'], '0')
                self.assertEqual(frame['referrerpolicy'], 'strict-origin-when-cross-origin')
                self.assertTrue(frame['title'])
                once = str(output)
                self.assertEqual(str(clean_html(output)), once)
                migrated.add(row['id'])
        self.assertEqual(migrated, {row['post_id'] for row in video_players() if 'alternative' not in row})

    def test_only_approved_alternative_videos_replace_original_ids(self):
        # Owner's selections: items 1-8 plus the recovered Scrum upload, twelve posts.
        approved = {908: '9y10Jvruc_Q', 906: '9y10Jvruc_Q', 848: 'U_HgMduuE5s',
                    465: 'vMV4PIEIKY4', 930: '1OnlF0X6G3g', 1168: '_tjYoKCBYag',
                    805: 'y9B75hH26yU', 540: '6gmP4nk0EOE', 542: '6gmP4nk0EOE',
                    1378: 'Bu8EtZdSJ3c', 910: '0nyF_4yMf28', 917: '0nyF_4yMf28'}
        self.assertEqual(len(video_players()), 20)
        self.assertEqual({r['post_id'] for r in video_players() if 'alternative' in r}, set(approved))
        for row in self.articles:
            if row['id'] not in approved:
                continue
            with self.subTest(article=row['slug']):
                original = BeautifulSoup(row['content']['rendered'], 'html.parser').find(['object', 'iframe', 'embed'])
                record = next(r for r in video_players() if r['post_id'] == row['id'])
                self.assertEqual(record['captured'], str(original))
                self.assertEqual(record['alternative']['url'], 'https://www.youtube.com/watch?v=' + approved[row['id']])
                output = clean_html(parse_document(row['content']['rendered']))
                self.assertEqual(len(output.find_all(['iframe', 'object', 'embed'])), 1)
                frame = output.iframe
                self.assertEqual(frame['src'].split('?')[0], 'https://www.youtube.com/embed/' + approved[row['id']])
                for dimension in ('width', 'height'):
                    size = original.get(dimension) or re.search(dimension + r'\s*:\s*(\d+)px', original.get('style', ''))[1]
                    self.assertEqual(frame[dimension], size)
                if 'video.google.com' in original.get('src', ''):
                    options = {'hl': ['en']}
                    if row['id'] == 465:
                        options['cc_load_policy'] = ['1']
                    self.assertEqual(parse_qs(urlsplit(frame['src']).query), options)
                self.assertTrue(frame.has_attr('allowfullscreen'))
                self.assertEqual(frame['referrerpolicy'], 'strict-origin-when-cross-origin')
                once = str(output)
                self.assertEqual(str(clean_html(output)), once)

    def test_mojiti_replacements_explain_missing_layers_and_preserve_article_content(self):
        for row in self.articles:
            output = clean_html(parse_document(row['content']['rendered']))
            notes = output.select('.archive-video-note')
            if row['id'] not in (540, 542):
                self.assertEqual(notes, [])
                continue
            with self.subTest(article=row['slug']):
                self.assertEqual(len(notes), 1)
                self.assertIs(output.iframe.find_next_sibling(), notes[0])
                text = notes[0].get_text()
                self.assertIn('Archive note:', text)
                self.assertIn('unavailable', text)
                self.assertIn('comments and clickable annotations' if row['id'] == 540
                              else 'transcription overlay', text)
                notes[0].decompose()
                actual = ' '.join(output.get_text(' ', strip=True).split())
                self.assertTrue(article_text_preserved(row['content']['rendered'], actual))
                if row['id'] == 540:
                    self.assertIsNotNone(output.find('img', src=re.compile('mojiti-web20-comment.png')))
                else:
                    self.assertIn('Complete transcript below', actual)
                    self.assertIn('[4:31]', actual)

    def test_video_check_detects_removed_players_and_changed_parameters(self):
        article = next(row for row in self.articles if row['slug'] == 'lessons-learned-from-pixar-2')
        source = article['content']['rendered']
        expected = expected_video_markup(article)
        for mutation in ('remove', 'url', 'dimensions', 'parameter'):
            with self.subTest(mutation=mutation):
                output = clean_html(parse_document(source))
                self.assertEqual(video_embed_markup(output), expected)
                if mutation == 'remove':
                    output.iframe.decompose()
                elif mutation == 'url':
                    output.iframe['src'] = 'https://www.youtube.com/embed/changed'
                elif mutation == 'dimensions':
                    output.iframe['width'] = '1'
                else:
                    output.iframe['src'] = output.iframe['src'].replace('rel=0', 'rel=1')
                self.assertNotEqual(video_embed_markup(output), expected)

    def test_unrelated_embeds_and_scripts_are_still_removed(self):
        source = '<iframe src="http://humanized.com/demo.html"></iframe><object data="example.swf"><embed src="example.swf"></object><applet></applet><script>tracking()</script>'
        output = clean_html(parse_document(source))
        self.assertIsNone(output.find(['iframe', 'object', 'embed', 'applet', 'script']))


if __name__ == '__main__':
    unittest.main()
