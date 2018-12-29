#!/usr/bin/env python
#coding:utf-8


""""
Name: 19_元组应用_两变量交换数据.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



# 元组应用的第一个场景:
x = 1
y = 2
x, y = y, x
# 1. 先把t = (y,x)封装为一个元组， 开辟了一个新的内存空间;
# 2. x = t[0] = 2
# 3. y = t[1] = 1
print(x,y)


# 2. 元组应用的第2个场景:
print("hello %s, hello %s" %("python", "c"))

t = ('python', 'c')
print("hello %s, hello %s" %t)






