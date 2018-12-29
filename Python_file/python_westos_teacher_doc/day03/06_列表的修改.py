#!/usr/bin/env python
#coding:utf-8


""""
Name: 06_列表的修改.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



names = ['fentiao', 'fendai', 'fensi', 'apple', 'fendai']


# 通过索引， 重新赋值；
names[0] = 'redhat'
print(names)

# 通过切片重新赋值
names[:2] = ['java', 'C']
print(names)


