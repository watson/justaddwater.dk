#!/usr/bin/env python3
"""Preview the archive with GitHub Pages' index.xml directory behavior."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class ArchiveHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        feed = Path(path) / 'index.xml'
        if not feed.is_file():
            return super().list_directory(path)
        self.send_response(200)
        self.send_header('Content-Type', 'application/xml')
        self.send_header('Content-Length', str(feed.stat().st_size))
        self.end_headers()
        return feed.open('rb')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--directory', default='site')
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(ArchiveHandler, directory=args.directory))
    print(f'Serving {args.directory} at http://127.0.0.1:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
