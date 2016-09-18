#coding:utf-8
#装饰器作为函数的缓存来使用
#2016/09/17



from functools import wraps
from  time import time
from time import sleep
import logging

#缓存装饰器定义
def cache(instance):
    def dec(fn):
        @wraps(fn)
        def wrap(*args,**kwargs):
            print('start run')
            start =time()
            p_args = ','.join([str(x) for x in args])
            kw_args = ','.join(['{}={}'.format(k,v) for k,v in sorted(kwargs.items())])
            key = '{}::{}::{}'.format(fn.__name__,p_args,kw_args)
            ret = instance.get(key)
            if ret is not None:
                print('{} run cast time :: {} seconds'.format(key, time() - start))
                return ret
            ret = fn(*args,**kwargs)
            instance.set(key,ret)
            print('{} run cast time :: {} seconds'.format(key,time() -start))
            return ret
        return wrap
    return dec

#缓存函数执行结果的字典类
class DictCache:
    def __init__(self):
        self.caches = {}
    def get(self,key):
        return self.caches.get(key)
    def set(self,key,value):
        self.caches[key] = value
    def __str__(self):
        return str(self.caches)
    def __repr__(self):
        return repr(self.caches)

#被装饰的主函数
@cache(instance=DictCache())
def long_time_fn(x):
    sleep(x)
    return x




if __name__ == '__main__':
    for i in range(4):
        long_time_fn(i)
    for j in range(4):
        long_time_fn(j)





