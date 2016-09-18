#coding:utf-8

import datetime
import random
import time

def tailf(path):
    offset=0
    while True:
        with open(path) as f:
            f.seek(offset)
            # for i in f:
            #     yield i
            yield from f #python3
            offset = f.tell()
        time.sleep(1)

for i in tailf('tt.py'):
    print(i)




