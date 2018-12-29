#!/usr/bin/env python
#coding:utf-8


""""
Name: 23_字符串的内置方法.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

print(min('hHello'))
print(max('hello'))


# python3中， 只支持数值类型比较大小;
# print(cmp('a', 'b'))


for i,j in enumerate("hello"):
    print(i,j)



s1 = "hello"
s2 = "worldhs"
for i in zip(s1, s2):
    print(i)

print(len("hello"))   # 求字符串长度



