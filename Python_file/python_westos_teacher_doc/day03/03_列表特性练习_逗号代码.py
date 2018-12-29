#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_列表特性练习_逗号代码.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


假定有下面这样的列表:
    names = ['fentiao', 'fendai', 'fensi', 'apple']

    输出结果为:'I have fentiao, fendai, fensi and apple.'


考察点:
    切片:
    字符串的join方法:

"""

# ','.join(names)

names = ['fentiao', 'fendai', 'fensi', 'apple']
print("I have " + ",".join(names[:-1]) + ' and ' + names[-1])

# 求列表的长度
# print(len(names))




