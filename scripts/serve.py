"""Serve only the built export, with real 404 responses and preview noindex headers."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=4321)
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent / 'dist'
if not (root / 'index.html').exists():
    parser.error('Run npm run build first.')

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
        if self.path.endswith(('.html', '/')):
            self.send_header('X-Robots-Tag', 'noindex, follow')
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            body = (root / '404.html').read_bytes()
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            if self.command != 'HEAD':
                self.wfile.write(body)
        else:
            super().send_error(code, message, explain)

print(f'Preview: http://127.0.0.1:{args.port}', flush=True)
ThreadingHTTPServer(('127.0.0.1', args.port), partial(Handler, directory=str(root))).serve_forever()
