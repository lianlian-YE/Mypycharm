#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_集合练习_华为机试题.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:




(华为机试题)题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，
他先用计算机生成了N个1到1000之间的随机整数（N≤1000）, N是用户输入的，对于
其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应
着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺
序去找同学做调查。请你协助明明完成“去重”与“排序”的工作;


count: 100


1, 4, 34,


# 在1-1000之间随机生成10个数字
random.sample(range(1,1000), 10)


sorted()
li.sort()
"""
import random

# print(random.sample(range(1,1000), 10))
# print(random.randint(1,1000))


# 将input接收的str，清值转化为int类型;
N = int(input("N："))
# list, set, tuple(x)

# 定义空集合时， 不能为s={}, 应该是s = set()
s = set()

for i in range(N):   # 4, (0,1,2,3)
    num = random.randint(1,1000)
    # 将随机生成的数加入到集合中;
    s.add(num)
# 对集合进行排序;
print(sorted(s))