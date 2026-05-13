#!/usr/bin/env python3
"""Tiny server for audiobook-tracker: serves files + provides save API."""
import http.server, json, os, sys, pathlib

DIR = pathlib.Path(__file__).parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(DIR), **kw)

    def do_POST(self):
        if self.path == '/api/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                self.send_response(400); self.send_header('Content-Type','text/plain'); self.end_headers()
                self.wfile.write(b'Invalid JSON'); return

            # Write data.json
            with open(DIR / 'data.json', 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            # Write source-data.js
            js = f"// Auto-generated — DO NOT EDIT\nwindow.SOURCE_DATA = {json.dumps(data, ensure_ascii=False)};\n"
            with open(DIR / 'source-data.js', 'w') as f:
                f.write(js)

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True, "series": len(data)}).encode())
            print(f"  💾 Saved {len(data)} series to data.json + source-data.js")
        else:
            self.send_response(404); self.end_headers()

    def log_message(self, format, *args):
        if '/api/' not in str(args[0]):
            super().log_message(format, *args)

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8420
    print(f"📚 Audiobook Tracker: http://localhost:{port}")
    http.server.HTTPServer(('127.0.0.1', port), Handler).serve_forever()
