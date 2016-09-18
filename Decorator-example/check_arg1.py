#coding:utf-8

from functools import wraps
from  time import time
from time import sleep
import logging
import inspect




def type_check(fn):
    @wraps(fn)
    def wrap(*args,**kwargs):
        for i,v in enumerate(inspect.signature(fn).parameters.values()):
            if v.annotation:
                if v.name in kwargs.keys():
                    if not isinstance(kwargs[v.name],v.annotation):
                        raise TypeError(v.name)
            else:
                if not isinstance(args[i],v.annotation):
                    raise TypeError(v.name)
        ret = fn(*args,**kwargs)
        return ret
    return wrap


@type_check
def add(x:int,y:int):
    return x + y

print(add(1,y = 2))
