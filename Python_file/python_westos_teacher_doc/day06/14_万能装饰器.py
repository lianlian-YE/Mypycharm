#!/usr/bin/env python
#coding:utf-8


""""
Name: 14_万能装饰器.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import time
import functools

# 需求: 编写一装饰器timeit, 用来装饰某函数执行时间的装饰器;
def timeit(fun):  # fun = world
    # 2. 注意: functools.wraps(fun): 可以保留add， world等函数的函数名， 帮助文档等属性信息;
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):    # kwargs = {'a':1, 'b':2}
        """
        this is wrapper function。。。。
        :param args:
        :param kwargs:
        :return:
        """
        start_time = time.time()
        temp = fun(*args, **kwargs)         # world(a=1, b=2)
        end_time = time.time()
        print("%s函数运行时间为%s" % (fun.__name__, end_time - start_time))
        return temp

    return wrapper

@timeit  # hello = timeit(hello)        # hello = wrapper
def hello():
    time.sleep(0.04)
    print("hello")


@timeit   # add = timeit(add)     # add = wrapper
def add(x,y):
    """
    add(x:int, y:int)->int:
    :param x:
    :param y:
    :return:
    """
    return x+y
# hello()  # wrapper()
print(add(1,3))


print(add.__name__)
print(add.__doc__)


@timeit         # world = timeit(world)   # world =  wrapper
def world(**kwargs):
    """this is **kwargs test"""
    return kwargs


print(world(a=1, b=2))
print(world.__name__)
print(world.__doc__)