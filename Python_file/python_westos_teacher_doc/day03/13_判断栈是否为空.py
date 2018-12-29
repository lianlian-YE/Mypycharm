#!/usr/bin/env python
#coding:utf-8


""""
Name: 13_判断栈是否为空.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



stack = []

if stack == []:
    print('NULL')
else:
    print("Not Null")
#
print(bool([]))
print(bool([1,2,3]))
if stack:
    print(stack)
else:
    print('NULL')

if not stack:
    print('null')
