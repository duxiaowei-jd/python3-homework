#coding:utf-8
#使用装饰器记录重要函数的执行所需要的时间
#2016/09/17

from functools import wraps
from  time import time
from time import sleep
import logging


#监控装饰器
def mertic(prefix,instance):
    def timeIt(fn):
        @wraps(fn)
        def wrap(*args,**kwargs):
            start = time()
            key = '{}.{}.{}'.format(prefix,fn.__module__,fn.__name__)
            ret = fn(*args,**kwargs)
            instance.send(key,time() - start)
            return ret
        return wrap
    return timeIt

#记录监控信息类
class LoggingMertic:
    def send(self,key,value):
        logging.info('{} cast ***{} seconds***'.format(key,value))

#需要被装饰的主函数
@mertic('magedu',instance=LoggingMertic())
def long_time_fun(x):
    sleep(x)
    return x

long_time_fun(3)




