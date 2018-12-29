#!/usr/bin/env python
#coding:utf-8


""""
Name: 04_系统内置queue使用.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

import queue



q = queue.Queue()

print(q.empty())
q.put("hello")
q.put("hello1")
q.put("hello2")


print(q.get())




