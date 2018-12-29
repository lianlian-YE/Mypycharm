#!/usr/bin/env python
#coding:utf-8


""""
Name: 04_continue范例.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# cotinue跳出本次循环， 继续执行；
# break： 跳出整个循环
tryCount = 0
while tryCount < 10:
    tryCount += 1
    if tryCount == 2:
        continue
    print(tryCount)