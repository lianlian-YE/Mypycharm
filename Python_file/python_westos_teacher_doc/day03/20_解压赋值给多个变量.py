#!/usr/bin/env python
#coding:utf-8


""""
Name: 20_解压赋值给多个变量.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 元组的赋值
t = ('fentiao', 5, 18)
name, age, weight = t
print(name, weight,age )


li = ['fentiao', 5, 18]
name, age, weight = li
print(name, weight,age )






scores = [100, 89, 90, 89, 67, 109]
# 列表的排序
scores.sort()
# python2中*middle是不能使用的;
min_score, *middle, max_score = scores
print("最终成绩为:%s" %(sum(middle)/4))





