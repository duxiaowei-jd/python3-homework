#coding:utf-8

from functools import wraps
from  time import time
from time import sleep
import logging
import inspect



def partial(fn,*args,**kwargs):
    @wraps(fn)
    def wrap(*p_args,**p_kwargs):
        return fn(*args,*p_args,**kwargs,**p_kwargs)
    return wrap

def add(x,y):
    return x + y

inc = partial(add,y=1)
print(inc(5))
