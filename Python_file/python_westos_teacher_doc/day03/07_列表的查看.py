#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_列表的查看.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
names = ['fentiao', 'fendai', 'fensi', 'apple', 'fendai', 'A', 'a', 'ab', 'Ab']

# 查看指定元素的索引值;
print(names.index('fentiao'))
print(names.count('fendai'))


# 按照指定的ASCII码进行排序的;
# names.sort()
# print(names)


# 不区分大小写进行排序;
names.sort(key=str.lower)
print(names)


# 列表的反转； 类似于li[::-1]
li = [10, 3, 89, 80]
li.reverse()
print(li)