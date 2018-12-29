#!/usr/bin/env python
#coding:utf-8


""""
Name: 14_内置方法.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:

min, max, sorted, reversed, zip, enumerate
"""



print(min([2, 1,2,343,545,6]))
print(max([2, 1,2,343,545,6]))
print(sum([2, 1,2,343,545,6]))
print(sorted([2, 1,2,343,545,6]))
for i in reversed([2, 1,2,343,545,6]):
    print(i,end=',')
print('\n')

for i in zip([1,2,3], ['a','b', 'c']):
    print(i, end=',')
print()
# 枚举， 返回列表的索引及对应的元素值;
for i in enumerate(['a', 'b', 'c']):
    print(i,end=' ')
