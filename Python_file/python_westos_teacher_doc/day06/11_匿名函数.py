#!/usr/bin/env python
# coding:utf-8


""""
Name: 11_匿名函数.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


#   1. 匿名函数的关键字为  lambda, 冒号前面是形式参数， 冒号后面是返回值;
#   2. 匿名函数的形式参数可以是: 必选， 默认， 可变， 关键字参数
"""
# 1). 无参数
f = lambda : "hello"
print(f())


f1 = lambda x, y=2: x**y
print(f1(2))
print(f1(2,3))


f2 = lambda  *args: sum(args)
print(f2(1,2,3,4,5))


f3 = lambda  **kwargs: kwargs
print(f3(a=1, b=2))


f4 = lambda x,y=2,*args,**kwargs: (x,y,args,kwargs)
print(f4(2,3,4,5,a=1,b=2))



from functools import reduce
def add(x, y):
    return x + y


# myadd = lambda x,y:x+y
# print(myadd(1,2))
print(reduce(lambda x, y: x + y, range(5)))


def mypow(x):
    return x ** 2


print(list(map(lambda x: x ** 2, range(5))))


#
# def isodd(num):
#     if num %2 == 0:
#         return True
#     else:
#         return False

def is_odd(num):
    return num % 2 == 0


print(list(filter(lambda x: x % 2 == 0, range(10))))

info = [
    ['001', 'apple', 1000, 2],
    ['002', 'xiaomi', 10, 2000],
    ['003', 'Oppo', 200, 1900],
    ['004', 'computer', 900, 5000]
]


def sorted_by_count(item):
    return item[2]


print(sorted(info, key=lambda x: x[2]))


def move_zero(item):
    if item == 0:
        return 1
    else:
        return 0
