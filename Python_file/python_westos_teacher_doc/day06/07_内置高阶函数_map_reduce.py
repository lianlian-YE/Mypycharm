#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_内置高阶函数_map_reduce.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:

高阶函数: 实参可以是一个函数; 返回值可以是一个函数;

普通函数:

# 函数定义:
        def 函数名(形参):   def add(a, b):
            函数体
            return 返回值   return 1

# 调用函数;
    函数名(实参)     add(1,2)
    print(函数名(实参) )


"""

# print(abs(-5))
#
# a = abs
# print(a(-5))


# 内置高阶函数



# 1. map函数理解
from collections import Iterable
# def func(x):
#     return x**2
#
# f = map(func, [0,1,2,3,4])
# # print(isinstance(f, Iterable))
# for i in f:
#     print(i)



# 1. map函数练习
# 需求： 用户接收一串数字； '1 3 5 7 8', 将该字符串中的所有数字转化为整形，并以列表格式输出;
s = '1 3 5 7 8'
# a, b, c, d, e = list(map(int, s.split()))
# print(a,e)


print([int(i) for i in s.split()])



# reduce： python2.x有， python3.x取消
# reduce在python3.x不是内置高阶函数， 而是需要导入from functools import reduce;

# In [2]: def add(x,y):
#    ...:     return x+y
#    ...:
#
# In [3]: reduce(add, [1,2,3,4,5,6])
# Out[3]: 21
#
# In [4]: (((1+2)+3)+4)

#
# from functools import reduce
# # def add(x,y):
# #     return x+y
# # print(reduce(add, range(5)))
#
#
# # 需求: 用户输入数字n； 求n的阶乘;  5!= 1*2*3*4*5
#
# def func(x,y):
#     return x*y
# print(reduce(func, range(1,6)))   # func(func(1,2),3)
#
