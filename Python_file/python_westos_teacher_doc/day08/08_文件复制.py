#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_文件复制.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:




"""


import random
import functools
import time

def timeit(fun):    # fun=add
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):  # 1,2   args=(1,2)
        """wrapper functions"""
        start_time = time.time()
        res = fun(*args, **kwargs)    # 参数解包add(*args, **kwargs)
        end_time = time.time()
        print("%s运行时间为%ss" %(fun.__name__,end_time-start_time))
        return res
    return wrapper


@timeit
def copy(sourcefile, destfile):
    with open(sourcefile) as f1:
        content = f1.read()
        with open(destfile,'w') as f2:
            f2.write(content)

@timeit
def copy1(sourcefile, destfile):
    # 要点: python2.7及以后，with支持对多个文件的上下文管理;
    with open(sourcefile) as f1, open(destfile,'a+') as f2:
        for line in f1:
            f2.write(line)
    print("拷贝 %s 为 %s 成功" %(sourcefile,destfile))

copy('ips.txt', 'hello_ips1.txt')
copy1('ips.txt', 'hello_ips2.txt')










