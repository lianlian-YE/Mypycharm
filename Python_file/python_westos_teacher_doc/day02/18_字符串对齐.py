#!/usr/bin/env python
# coding:utf-8


""""
Name: 18_字符串对齐.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:

ljust， rjust， center, format
"""

print("学生管理系统".center(30))
print("学生管理系统".center(30, "*"))
print("学生管理系统".center(30, "#"))
print("学生管理系统".ljust(30, "*"))
print("学生管理系统".rjust(30, "*"))

print("hello %s" %('world'))
# 位置参数
print("{0} {1} {0} {0}".format(1,2))






