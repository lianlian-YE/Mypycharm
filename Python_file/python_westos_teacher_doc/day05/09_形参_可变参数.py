#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_形参_可变参数.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# 可变参数, *变量名;
# *args, args实质是一个元组；
def mySum(*args):
    print(args, type(args))
    return  sum(args)


print(mySum(1,2,3,4,5))


# 如果已经存在；列表， 但是要把列表的每一个元素作为参数， 可以直接*li进行解包;
# li = range(1,1001)
# li = (1,2,3)

li = {1,2,3}
print(mySum(*li))