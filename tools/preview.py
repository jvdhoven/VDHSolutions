#!/usr/bin/env python3
"""
VDH Solutions - Local Preview Server
Serves the website locally so you can preview both English (/) and Dutch (/nl/) versions.
Usage:
    python3 tools/preview.py [PORT]
"""

import http.server
import os
import socketserver
import sys
import webbrowser

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=REPO_ROOT, **kwargs)

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT

    # Attempt to bind to requested port or next available
    for p in range(port, port + 10):
        try:
            httpd = socketserver.TCPServer(("", p), CustomHandler)
            port = p
            break
        except OSError:
            continue
    else:
        print(f"Error: Could not bind to port {port} or next 10 ports.")
        sys.exit(1)

    url_root = f"http://localhost:{port}/"
    url_nl = f"http://localhost:{port}/nl/"

    print("=" * 55)
    print("  VDH Solutions - Local Preview Server Running")
    print("=" * 55)
    print(f"  English:  {url_root}")
    print(f"  Dutch:    {url_nl}")
    print("  Press Ctrl+C to stop the server.")
    print("=" * 55)

    try:
        # Open in default browser if interactive
        webbrowser.open(url_root)
    except Exception:
        pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == "__main__":
    main()
