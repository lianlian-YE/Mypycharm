#!/usr/bin/env python
# coding:utf-8


""""
Name: 10_字符串的定义方式.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

a = "hello"
b = 'westos'
c = """
                用户管理系统
                
    1). 添加用户                
    2). 删除用户                
    3). 显示用户                
"""

print(type(a))
print(type(b))
print(type(c))

print(c)

# 2. 字符串常用的转义符号:
#   \n:换行
#   \t: 一个tab键
#   \': '
#   \": "

# 打印"hello"
# 打印guido's
# 打印"hello guido's python"


print('"hello"')
print("guido's")
print("\"hello guido\'s python\"")

print("%s\t%s" % ("hello", "world"))
