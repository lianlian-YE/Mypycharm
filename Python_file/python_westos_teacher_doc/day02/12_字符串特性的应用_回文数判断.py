#!/usr/bin/env python
# coding:utf-8


""""
Name: 12_字符串特性的应用_回文数判断.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


##  题目要求:
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样
的整数。

## 示例:

示例 1:
        输入: 121
        输出: true
示例 2:
        输入: -121
        输出: false
        解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
        输入: 10
        输出: false
        解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？





"""
# 方法1：
# # 121  ==  121
# num = input('Num:')
# print(num == num[::-1])




# 方法2： 无需将整形转化为字符串类型
num = int(input('Num:'))

# 如果为负数 或者为10，20，30....不是回文数;
if num < 0 or (num!=0 and num%10 == 0):
    print(False)
# 0是回文数;
elif num == 0:
    print(True)
else:
    back = 0
    while num > back:
        back = back * 10 + num % 10
        num //= 10     # num = num / 10
    print(num == back or num == back//10)
