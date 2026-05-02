#!/usr/bin/env python3
import http.server
import os
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get("PORT", 8080))

class LoggingHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(f"{self.address_string()} - [{self.log_date_time_string()}] {fmt % args}", flush=True)

with http.server.HTTPServer(("0.0.0.0", port), LoggingHandler) as server:
    print(f"Serving on 0.0.0.0:{port}", flush=True)
    server.serve_forever()
