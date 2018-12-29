#!/usr/bin/env python
# coding:utf-8


""""
Name: 09_sorted函数应用_携程笔试_移动数组中的0.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:
# (2018-携程-春招题)题目需求:
给定一个整形数组， 将数组中所有的0移动到末尾， 非0项保持不变；
在原始数组上进行移动操作， 勿创建新的数组;
# 输入:
    第一行是数组长度， 后续每一行是数组的一条记录;
    4
    0
    7
    0
    2
# 输出:
    调整后数组的内容;
    7
    2
    0
    0
"""

n = int(input("数组长度:"))
li = [int(input()) for i in range(n)]
for i in sorted(li, key=lambda x: 1 if x is 0 else 0): print(i)
# def move_zero(item):
#     if item == 0:
#         return 1
#     else:
#         return 0
#
# for i in sorted(li, key=move_zero):
#     print(i)
