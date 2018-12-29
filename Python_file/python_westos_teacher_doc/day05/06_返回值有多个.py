#!/usr/bin/env python
#coding:utf-8


""""
Name: 06_返回值有多个.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



def fun(a):   # a = [34, 1, 2, 3, 4, 5, 6, 7, 2378]
    # 我接收一个列表， 求这个列表的最大值，平均值， 最小值;
    max_num  = max(a)
    min_num = min(a)
    avg_num = sum(a)/len(a)

    # python函数中， 只能返回一个值;
    # 如果非要返回多个值， 会把返回的值封装为一个元组数据类型;
    return max_num, avg_num, min_num


variables  = fun([34, 1, 2, 3, 4, 5, 6, 7, 2378])
print(variables, type(variables))
