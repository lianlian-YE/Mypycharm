#!/usr/bin/env python
# coding:utf-8


""""
Name: mytime.py
Date: 2018/06/10
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import time
from functools import wraps


def timeit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print("%s run %.2fs" % (f.__name__, end - start))
        return res

    return wrapper
