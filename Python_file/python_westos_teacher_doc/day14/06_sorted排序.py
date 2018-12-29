#!/usr/bin/env python
# coding:utf-8


""""
Name: 06_sorted排序.py
Date: 2018/06/03
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

li = [
    ['001', 'apple', 2000, 2],
    ['007', 'xiaomi', 100, 999],
    ['003', 'huawei', 300, 1999]
]

# def sorted_by_count(item):
#     return item[2]

# print(sorted(li, key=sorted_by_count))
print(sorted(li, key=lambda item: item[2], reverse=True))
