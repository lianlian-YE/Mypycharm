#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_fib数列生成器的实现.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
# 1. 当在函数中看到yield关键字， 那么这个函数调用的返回值是一个生成器;


def fib(num):
    a, b, count = 0, 1, 1  # 0, 1
    while count <= num:
        yield b
        a, b = b, a + b  #a=2, b=3
        count += 1

g = fib(10)
for i in g:
    print(i)