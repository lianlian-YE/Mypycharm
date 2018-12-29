#!/usr/bin/env python
# coding:utf-8


""""
Name: 17_字符串删除不需要的子符_应用于读取及清洗数据中.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


strip, lstrip, rstrip, replace
"""


# strip： 删除字符串左边和右边的空格; 在这里空格是广义的: \n,\t,
s = " \t \n            hello    jhfkjhgkjrhgk  \nkjhkjrhgruhg"
print(s.strip())

# lstrip:删除字符串左边的空格;rstrip:删除字符串右边的空格
s = " \t \n            hello    jhfkjhgkjrhgk  \nkjhkjrhgruhg\n\t"
print(s.lstrip())

# 如何删除中间的空格?  # 通过replace间接实现
s = "hello world hello"
print(s.replace(" ", ""))





