#!/usr/bin/env python
#coding:utf-8


""""
Name: 06_装饰器总结.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:

# 1. 什么是装饰器?

# 2.
@add_log    # fun = add_log(fun)
def fun():
    return "fun"

#3. 装饰器模板


## 3-1. 装饰器函数不加参数:
def 装饰器名称(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        # 函数执行之前做的操作
        res =  fun(*args, **kwargs)
        # 函数执行之前做的操作
        return res
    return wrapper


## 3-2. 装饰器函数加参数:


def  装饰器名称(*args, **kwargs):
    def inner(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            # 函数执行之前做的操作
            res =  fun(*args, **kwargs)
            # 函数执行之前做的操作
            return res
        return wrapper
    return inner

# 4. import functools
    @functools.wraps(f)


# 5. import inspect
inspect.getcallargs(f,*args,**kwargs)


# 6. 多个装饰器时

@deco1      #fun =  deco1(fun)
@deco2     # fun = deco2(fun)
def fun():
    return "fun"

"""


