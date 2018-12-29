#!/usr/bin/env python
# coding:utf-8


""""
Name: 12_高阶函数_返回值是函数的.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

#
# def compare(base, y):
#     return base > y
# print(compare(5,3))
# print(compare(5,20))




# # 闭包: 函数里面嵌套函数;
# def compare1(base):
#     def compare2(y):
#         return base > y
#     return compare2
# compare_base_10 = compare1(10)
# print(compare_base_10(3))
# print(compare_base_10(20))



# 装饰器: 器:函数, 类; 用来装饰函数的东西;

# 产品经理， 开发人员(ATM)

# 母亲节..... 六一.......
# for i in 'hello':
#     print(i)

# 装饰器应用场景: 如果你想在执行函数之前做什么或者执行函数之后做什么， 建议使用装饰器;
def add_info(fun):  # fun = saveMoney
    def wrapper():
        print("六一......")
        print("欢迎ICBC银行ATM........")
        fun()    # saveMoney()
    return wrapper

# python的语法糖
@add_info    # saveMoney= addinfo(saveMoney)
def saveMoney():
    print("存钱.......")
saveMoney()
# @add_info
# def transferMoney():
#     print("转账......")
#
#
# def getMoney():
#     print("取钱.......")





"""
此处省略1000个函数.........
"""







