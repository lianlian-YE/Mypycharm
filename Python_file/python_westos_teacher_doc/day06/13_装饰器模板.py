#!/usr/bin/env python
# coding:utf-8


""""
Name: 13_装饰器模板.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import time

import functools


def add_info(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        # 函数执行之前做的操作
        res =  fun(*args, **kwargs)
        # 函数执行之前做的操作
        return res
    return wrapper


# 需求: 编写一装饰器timeit, 用来装饰某函数执行时间的装饰器;
def timeit(fun):  # fun = add
    def wrapper(x,y):
        start_time = time.time()
        fun(x,y)   # hello()
        end_time = time.time()
        print("%s函数运行时间为%s" % (fun.__name__, end_time - start_time))
    return wrapper
@timeit  # hello = timeit(hello)        # hello = wrapper
def hello():
    time.sleep(0.04)
    print("hello")

@timeit   # add = timeit(add)     # add = wrapper
def add(x,y):
    return x+y
hello()  # wrapper()
print(add(1,3))
