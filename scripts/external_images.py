#!/usr/bin/env python3
"""Preserve public external raster images referenced by the archived articles."""
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from archive import ROOT, SITE, HOSTS, ORIGIN, CACHE, CSS_URL, IMAGE_SUFFIXES, embedded_css, fetch, write_json


def download(url):
    parts = urlsplit(url)
    if parts.scheme not in ('http', 'https') or not parts.hostname or parts.username or parts.password:
        raise ValueError('Not a plain public HTTP image URL')
    candidates = [urlunsplit(parts._replace(scheme='https'))]
    if parts.scheme == 'http':
        candidates.append(url)
    errors = []
    for candidate in candidates:
        try:
            req = Request(candidate, headers={'User-Agent': 'justaddwater-static-archive/1.0'})
            with urlopen(req, timeout=10) as response:
                body = response.read(15 * 1024 * 1024 + 1)
            if len(body) > 15 * 1024 * 1024:
                raise ValueError('Image exceeds 15 MiB')
            if body.startswith(b'\x89PNG\r\n\x1a\n'):
                extension = '.png'
            elif body.startswith(b'\xff\xd8\xff'):
                extension = '.jpg'
            elif body.startswith((b'GIF87a', b'GIF89a')):
                extension = '.gif'
            elif body.startswith(b'RIFF') and body[8:12] == b'WEBP':
                extension = '.webp'
            else:
                raise ValueError('Response is not a supported raster image')
            path = '/archive-assets/external/' + hashlib.sha256(body).hexdigest()[:24] + extension
            target = SITE / path.lstrip('/')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
            return {'path': path, 'fetched_from': candidate, 'sha256': hashlib.sha256(body).hexdigest()}
        except Exception as error:
            errors.append(str(error))
    raise ValueError('; '.join(dict.fromkeys(errors)))


def capture():
    data = json.loads((ROOT / 'data/content.json').read_text())
    urls = set()
    def collect(soup):
        candidates = [image['src'] for image in soup.find_all(['img', 'input'], src=True)
                      if image.name == 'img' or image.get('type', '').lower() == 'image']
        candidates.extend(link['href'] for link in soup.find_all('a', href=True)
                          if Path(urlsplit(link['href']).path).suffix.lower() in IMAGE_SUFFIXES)
        candidates.extend(match[2] for css in embedded_css(soup) for match in CSS_URL.finditer(css))
        urls.update(url for url in candidates if urlsplit(url).hostname and urlsplit(url).hostname not in HOSTS)

    for row in data['posts'] + data['pages']:
        soup = BeautifulSoup(row['content']['rendered'], 'html.parser')
        collect(soup)
    # Theme chrome, attachment pages and comments can contain images that aren't
    # part of a post's API content (for example the original RSS icon).
    capture_file = CACHE / 'capture.json'
    if capture_file.exists():
        state = json.loads(capture_file.read_text())
        for path in set(state['pages']) | set(state['assets']):
            raw, _ = fetch(ORIGIN + path)
            if path in state['pages'] or Path(path).suffix.lower() in ('.html', '.htm'):
                collect(BeautifulSoup(raw, 'html.parser'))
            elif path.endswith('.css'):
                urls.update(match[2] for match in CSS_URL.finditer(raw.decode('utf-8', 'replace'))
                            if urlsplit(match[2]).hostname and urlsplit(match[2]).hostname not in HOSTS)
    results_file = ROOT / 'data/external-images.json'
    results = json.loads(results_file.read_text()) if results_file.exists() else {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        pending = {pool.submit(download, url): url for url in sorted(urls) if url not in results}
        for future in as_completed(pending):
            url = pending[future]
            try:
                results[url] = future.result()
            except Exception as error:
                results[url] = {'error': str(error)}
            if len(results) % 20 == 0:
                print(f'External images checked: {len(results)}/{len(urls)}', flush=True)
            write_json(results_file, results)
    print(f'External images: {sum("path" in r for r in results.values())} recovered / {len(results)} referenced')


if __name__ == '__main__':
    capture()
