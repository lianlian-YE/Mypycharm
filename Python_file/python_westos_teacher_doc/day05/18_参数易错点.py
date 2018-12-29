#!/usr/bin/env python
#coding:utf-8


""""
Name: 18_参数易错点.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



# 定义函数， 默认参数的默认值尽量不是可变参数;
def fun(li=[]):
    li.append("hello")
    return li


print(fun())
print(fun())

