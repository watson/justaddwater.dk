"""Guard the report's distinctions between recovery, preservation and evidence."""
import json
from pathlib import Path
import unittest

from migration_report import Page, dependency_closure, image_outcome
from bs4 import BeautifulSoup
from verify import report_reference_allowed

ROOT = Path(__file__).resolve().parents[1]


class ReportTests(unittest.TestCase):
    def test_source_link_exception_cannot_allow_a_remote_load_or_article_link(self):
        url = 'http://justaddwater.dk/old.jpg'
        soup = BeautifulSoup(f'<a data-migration-reference="true" href="{url}">Source</a><img data-migration-reference="true" src="{url}">', 'html.parser')
        self.assertTrue(report_reference_allowed(soup.a, 'href', '/migration-report/index.html', {url}))
        self.assertFalse(report_reference_allowed(soup.img, 'src', '/migration-report/index.html', {url}))
        self.assertFalse(report_reference_allowed(soup.a, 'href', '/article/index.html', {url}))
        self.assertFalse(report_reference_allowed(soup.a, 'href', '/migration-report/index.html', set()))

    def test_failed_download_is_never_counted_as_recovered(self):
        self.assertEqual(image_outcome({'error': '404', 'missing_path': '/missing/a.jpg'}), 'Not recovered')
        self.assertEqual(image_outcome({'path': '/a.jpg', 'fetched_from': 'https://publisher.example/a.jpg'}),
                         'Saved from publisher or image host')
        self.assertEqual(image_outcome({'path': '/a.jpg', 'fetched_from': 'https://web.archive.org/web/2006/http://old/a.jpg'}),
                         'Recovered from Internet Archive')

    def test_only_real_markup_is_indexed_and_css_imports_are_followed(self):
        page = Page('/demo/', '<link href="/map.css"><pre>&lt;img src="/fake.png"&gt;</pre><img src="../a%20b.jpg"><style>.a{background:url(/real.png)}</style>')
        self.assertNotIn('/fake.png', page.refs)
        self.assertIn('/a b.jpg', page.refs)
        self.assertIn('/real.png', page.refs)
        refs = dependency_closure(page.refs, {'/map.css': {'/nested.css'}, '/nested.css': {'/map.css', '/sprite.png'}})
        self.assertIn('/sprite.png', refs)

    def test_every_successful_image_and_stylesheet_record_is_present(self):
        report = json.loads((ROOT / 'data/migration-report.json').read_text())
        local = {r['source'] for r in report['resources']}
        for name in ('external-images', 'external-resources'):
            records = json.loads((ROOT / f'data/{name}.json').read_text())
            if name == 'external-resources':
                records = records['resources']
            for source, record in records.items():
                self.assertEqual(source in local, bool(record.get('path')), source)

    def test_videos_and_private_exports_are_not_local_preservation_claims(self):
        report = json.loads((ROOT / 'data/migration-report.json').read_text())
        for resource in report['resources']:
            self.assertTrue(resource['source'].startswith(('http://','https://')), resource['source'])
            self.assertTrue(not resource['retrieved_from'] or resource['retrieved_from'].startswith(('http://','https://')))
            self.assertNotIn('youtube.com', resource['source'])
            self.assertNotIn('.cache/', resource['path'])
            self.assertNotIn('wordpress-export', resource['path'])
        for change in report['changes']:
            if change['id'].startswith('video-'):
                self.assertNotIn('preserved', change['categories'])
        self.assertTrue(report['unresolved'])
        self.assertTrue(all(not key.startswith('.cache/') for key in report['inputs']))

    def test_specific_records_have_locations_and_ids_are_unique(self):
        report = json.loads((ROOT / 'data/migration-report.json').read_text())
        for collection in ('changes', 'resources'):
            ids = [r['id'] for r in report[collection]]
            self.assertEqual(len(ids), len(set(ids)))
        for change in report['changes']:
            self.assertTrue(change['pages'], change['id'])
        for resource in report['resources']:
            if resource['kind'].startswith('Inline gist:'):
                # A page merely linking to the article is not a gist user.
                self.assertTrue(all(p == resource['path'] or p.startswith(resource['path'] + 'comment-page-') for p in resource['pages']))


if __name__ == '__main__':
    unittest.main()
