#!/usr/bin/env python
# coding:utf-8


""""
Name: 04_return的应用.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:

# 随机生成20个学生的成绩;
# 判断这20个学生成绩的等级;

"""
import random


def get_level(score):
    if 90 < score <= 100:
        return 'A'
    elif 80 < score <= 90:
        return 'B'
    else:
        return 'C'


def main():
    for i in range(20):
        score = random.randint(1,100)
        print("成绩为%s, 等级为%s" %(score,get_level(score)))




    # scores = []
    #
    # # 生成所有的成绩;
    # for count in range(20):
    #     scores.append(random.randint(1, 100))
    #
    #
    # # 根据所有的成绩判断等级；
    # for score in scores:
    #     print("成绩为%s, 等级为%s" %(score,get_level(score)))


main()
