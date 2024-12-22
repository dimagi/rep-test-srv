#!/bin/bash

if [ ${EUID} -ne 0 ]
then
    echo "Please run as root or with sudo"
    exit 1
fi

export QUART_REDIS_URI='redis://localhost:6379/0'

# Assumes external network device is eth0
IP_ADDR=$(ip addr | grep 'eth0:' -A2 | grep 'inet\b' | awk '{print $2}' | cut -d'/' -f1)
PORT=80

cd /opt/rep-test-srv/ || exit 1
source venv/bin/activate
hypercorn -b $IP_ADDR:$PORT http_resp:app
