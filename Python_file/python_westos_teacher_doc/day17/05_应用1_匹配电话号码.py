#!/usr/bin/env python
#coding:utf-8


""""
Name: 05_应用1_匹配电话号码.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:

1. 电话号码的规则为:
197-6745-5498
19767455498


2. “hello cfdjhvutorjfeoifjporejd18897655643dgfjhgfrihut 167-2443-8934”
"""


import re
# pattern = r'\d\d\d-?\d\d\d\d-?\d\d\d\d'
pattern = r'\d{3}-?\d{4}-?\d{4}'
s = "hello cfdjhvutorjfeoifjporejd18897655643dgfjhgfrihut 167-2443-8934"

print(re.findall(pattern, s))

