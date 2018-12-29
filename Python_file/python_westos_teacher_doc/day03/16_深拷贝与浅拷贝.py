#!/usr/bin/env python
# coding:utf-8


""""
Name: 16_深拷贝与浅拷贝.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
#
# li = [1,2,3,4]
#
# # 拷贝:
# # 不是拷贝， 是将li1的指向li的内存位置;
# li1 = li
# print(li1 is li)
#
#
# # 拷贝列表成功
# li2 = li[:]
# print(li2 is li)
# li2.append(5)
# print(li)
# print(li2)


# 浅拷贝
# li = [1, 2, 3, [2, 3]]
#
# li3 = li[:]
# print(li3 is li)
# print(li3[-1][0] is li[-1][0])
#
# li3[-1].append(0)
# print(li)
# print(li3)

import copy

li = [1, 2, 3, [2, 3]]
li3 = copy.copy(li)
li.append(1)





# 深拷贝
import copy
li = [1, 2, 3, [2, 3]]
li4 = copy.deepcopy(li)


print(li is li4)
li4[-1].append(0)
print(li)
print(li4)