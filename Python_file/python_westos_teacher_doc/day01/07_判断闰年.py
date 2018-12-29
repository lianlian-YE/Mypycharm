#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_判断闰年.py
Date: 2018/04/21
Connect: xc_guofan@163.com
Author: lvah
Desc:

用户输入year， 判断是否为闰年?
    year能被4整除但是不能被100整除 或者 year能被400整除， 那么就是闰年;



    整除:代表year%4 == 0
    不能整除: year%4 != 0

"""

year = int(input("Year:"))
if (year % 4 == 0  and year %100 !=0) or (year % 400 == 0):
    print("%s是闰年" %(year))
else:
    print("%s不是闰年" %(year))
