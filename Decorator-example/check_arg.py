#coding:utf-8
#使用装饰器进行参数检查

from functools import wraps
from  time import time
from time import sleep
import logging


def check_arg(*check_args,**check_kwargs):
    def dec(fn):
        @wraps(fn)
        def wrap(*args,**kwargs):
            for i ,t in enumerate(check_args):
                if not  isinstance(args[i],t):
                    print('position args:{},must be {} type'.format(i,t))
                    return False
            for k,w in check_kwargs.items():
                if not isinstance(kwargs[k],w):
                    print('kwargs :{},must be {} type'.format(k,w))
                    return False
            ret = fn(*args,**kwargs)
            return ret
        return wrap
    return dec

@check_arg(x = int,y = int)
def add(x,y):
    return x + y

print(add(x=1,y = '2'))
