#coding:utf-8

import datetime
import random
import time

def data_source():
    while True:
        yield random.randint(0,100)
        time.sleep(0.1)

ds = data_source()

def top_k(k,time=3):
    start = datetime.datetime.now()
    lst = []
    while True:
        lst.append(next(ds))
        current = datetime.datetime.now()
        if (current - start).total_seconds() >= time:
            start = current
            lst.sort()
            ret = []
            for _ in range(k):
                ret.append(lst.pop())
            yield ret
tp = top_k(10,4)
for _ in range(3):
    print(next(tp))

