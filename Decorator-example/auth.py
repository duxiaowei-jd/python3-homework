#coding:utf-8
#装饰器实现身份认证，例子是模拟不能运行
#2016/09/17

from functools import wraps
from  time import time
from time import sleep
import logging

def doAuth(info):
    return True

def AccessDenied():
    return 'deny you access !!!'

def auth(header_name):
    def dec(fn):
        @wraps(fn)
        def wrap(*args,**kwargs):
            info = request.headers.get(header_name)
            if doAuth(info):
                ret = fn(*args,**kwargs)
                return ret
            return AccessDenied()
        return wrap
    return dec

@auth('X-auth-Info')
def handle(request):
    pass



