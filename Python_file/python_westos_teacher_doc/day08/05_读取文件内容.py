#!/usr/bin/env python
#coding:utf-8


""""
Name: 05_读取文件内容.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



import time
import random
import functools

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
def open1():
    with open("/etc/passwd") as f:
        # f.readlines(), 会把文件的所有内容加载到内存中;s适用于小文件;
        for line in f.readlines():
            line.split(":")
@timeit
def open2():
    with open("/etc/passwd") as f:
        # 迭代----》 生成器
        for line in f:
            line.split(":")
open1()
open2()



