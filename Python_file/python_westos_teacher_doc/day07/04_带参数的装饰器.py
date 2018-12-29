#!/usr/bin/env python
#coding:utf-8


""""
Name: 04_带参数的装饰器.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:


# 1. 创建add_log装饰器， 被装饰的函数打印日志信息；
# 2. 日志格式为: [字符串时间] 函数名: xxx， 运行时间：xxx, 运行返回值结果:xxx

"""

import time
import functools
import random



# 带有参数的装饰器; 在原有装饰器外面加一个函数， 用来接收装饰器参数的;
def addLog(type):   # type='warn'
    # type="warn"    Warn
    # type.title()
    def add_log(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = f(*args, **kwargs)
            end_time = time.time()
            print("日志信息:[%s] [%s] %s 运行时间为%.5f s 运行结果为%s" %(
                type.title(),time.ctime(),f.__name__,end_time-start_time,res))
            return res
        return wrapper
    return add_log


@addLog("warn")   # hello = addLog(warn')
                        #  hello = add_log(hello)
                        # hello ======= wrapper()
def hello():
    time.sleep(random.random())
    return "hello"


@addLog(type="debug")
def add(x,y):
    time.sleep(random.random())
    return x+y

print(hello())
print(add(1,2))



