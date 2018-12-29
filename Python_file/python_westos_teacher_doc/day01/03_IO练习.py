#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_IO练习.py
Date: 2018/04/21
Connect: xc_guofan@163.com
Author: lvah
Desc:
# 求平均成绩
#   1. 用户输入某个学生的姓名；
#   2. 输入该学生的语文， 数学与英语的成绩；
#   3. 打印:   姓名的平均成绩为:
#   4. 平均成绩要求保留两位小数点;


"""
# from __future__ import division
#
#
# stuName = raw_input("姓名:")
# chinese = input("语文成绩:")
# math = input("数学成绩:")
# english = input("英语成绩:")
#
# avgScore = (chinese+math+english)/3
#
# print "%s的平均成绩:%.2f" %(stuName, avgScore)







# python3

stuName = input("姓名:")
# 强制转换接收的字符串为整形
chinese = int(input("语文成绩:"))
math = int(input("数学成绩:"))
english = int(input("英语成绩:"))

avgScore = (chinese+math+english)/3

print("%s的平均成绩:%.2f" %(stuName, avgScore))