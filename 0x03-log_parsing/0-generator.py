#!/usr/bin/python3
"""
generator script that
generate random log
"""
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    str0 = "{:d}.{:d}.{:d}.{:d}"
    str1 = str0 + " - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n"
    sys.stdout.write(str1.format(
        random.randint(1, 255),
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
