#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_函数定义与使用.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# 1. 无参数的函数;
#
# # 定义函数， 并不会执行;
# def hello():
#     # 函数体
#     print("hello")
#
# # 调用函数
# hello()
#


# print(len("hello"))
# print()



# 2. 带有参数的函数
def fun1(name):
    # name = "fentiao"
    # 定义函数时的变量称为形式参数， 变量名可以任意起；
    print("hello %s" %(name))



fun1("fendai")     # 调用函数时的参数称为实参, 该参数必须是实际存在的；


