#!/usr/bin/env python
#coding:utf-8


""""
Name: 15_return原理.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



def fun():
    print('hello')
    return "world"   # 在执行函数时， 遇到return， 函数就执行结束;return后面的永不执行;
    print('gcc')


print(fun())