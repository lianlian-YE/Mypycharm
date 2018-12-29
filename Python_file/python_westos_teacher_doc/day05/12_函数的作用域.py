#!/usr/bin/env python
#coding:utf-8


""""
Name: 12_函数的作用域.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 作用域：
#   局部作用域：
#   全局作用域

# 全局作用域:作用于整个脚本
num = 10
print("out fun: id=", id(num))

def fun():
    # 局部作用域, 在函数运行时生效， 函数运行结束则释放；
    num = 2
    print("in fun: id=", id(num))
    print("in fun: num = %s" %(num))

fun()
print("out fun: num =%s" %(num))



"""
1.  num = 10
2. fun
3. num = 2(当函数执行结束， 变量num的值2被释放掉)
4. num = 10

"""




