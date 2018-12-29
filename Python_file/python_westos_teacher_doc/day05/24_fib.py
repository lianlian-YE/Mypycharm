#!/usr/bin/env python
# coding:utf-8


""""
Name: 24_fib.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:
3.打印斐波那契数列列前十十列列,示例例如下(语言言不不限):
1 1 2 3 5 8 13 21 34 55 ....

"""


def fib(num):
    a, b, count = 0, 1, 1  # 0, 1
    while count <= num:
        print(b)
        a, b = b, a + b  #a=2, b=3
        count += 1


fib(90)