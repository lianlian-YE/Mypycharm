#!/usr/bin/env python
#coding:utf-8


""""
Name: 13_global关键字.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
num = 10


def fun():
    # 通过global关键字声明局部变量为全局变量， 让函数执行完， 2依旧生效;
    global num
    num = 2

fun()
print(num)





