#!/usr/bin/env python3
"""Capture public per-article RSS responses for offline feed generation."""
from concurrent.futures import ThreadPoolExecutor, as_completed
import html
import json
import re

from bs4 import BeautifulSoup
from archive import ROOT, ORIGIN, fetch, write_json, id_routes, local_url
from feeds import feed_specs, parse_comment_feed


def capture_post_ids(data):
    wanted = {row['id'] for row in data['posts']}
    pages = range(1, (len(wanted) + 99) // 100 + 1)
    def read(page):
        raw, _ = fetch(ORIGIN + f'/wp-json/wp/v2/posts?per_page=100&page={page}&_fields=id,guid')
        return {str(row['id']): html.unescape(row['guid']['rendered']) for row in json.loads(raw) if row['id'] in wanted}
    result = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for values in pool.map(read, pages):
            result.update(values)
    if set(map(int, result)) != wanted:
        raise ValueError('Missing original post feed IDs')
    write_json(ROOT / 'data/post-feed-ids.json', dict(sorted(result.items(), key=lambda pair: int(pair[0]))))
    print(f'Captured {len(result)} original post feed IDs.', flush=True)


def capture():
    data = json.loads((ROOT / 'data/content.json').read_text())
    capture_post_ids(data)
    state = json.loads((ROOT / '.cache/capture.json').read_text())
    # Some stale media records resolve to the homepage and have no attachment
    # feed. Preserve the feed URLs actually advertised by captured pages.
    paths = set()
    ids = id_routes(data)
    for path in state['pages']:
        raw, _ = fetch(ORIGIN + path)
        soup = BeautifulSoup(raw, 'html.parser')
        paths.update(local_url(tag['href'], ORIGIN + path, ids) for tag in soup.select('a[href], link[href]'))
    specs = {p: s for p, s in feed_specs(data, paths).items() if 'post_id' in s}
    known = set()
    for file in (ROOT / 'site').rglob('*.html'):
        known.update(map(int, re.findall(r'id="comment-(\d+)"', file.read_text())))

    def read(path):
        raw, meta = fetch(ORIGIN + path)
        items = parse_comment_feed(raw)
        unexpected = {i['id'] for i in items} - known
        if unexpected:
            raise ValueError(f'Feed contains responses not in the reviewed archive: {sorted(unexpected)}')
        return {'post_id': specs[path]['post_id'], 'captured_at': meta['captured_at'], 'items': items}

    result, failures = {}, {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(read, path): path for path in specs}
        for future in as_completed(futures):
            path = futures[future]
            try:
                result[path] = future.result()
            except Exception as error:
                failures[path] = str(error)
            if (len(result) + len(failures)) % 100 == 0:
                print(f'Feeds captured: {len(result)}; failures: {len(failures)}', flush=True)
    if failures:
        write_json(ROOT / '.cache/feed-capture-failures.json', failures)
        write_json(ROOT / '.cache/feed-capture-partial.json', result)
        raise SystemExit(f'{len(failures)} feeds need investigation; see .cache/feed-capture-failures.json')
    write_json(ROOT / 'data/comment-feeds.json', {'source': ORIGIN, 'feeds': dict(sorted(result.items()))})
    print(f'Captured {len(result)} feeds containing {sum(len(r["items"]) for r in result.values())} responses.')


if __name__ == '__main__':
    capture()
