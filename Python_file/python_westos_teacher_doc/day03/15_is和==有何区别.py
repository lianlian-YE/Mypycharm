#!/usr/bin/env python
#coding:utf-8


""""
Name: 15_is和==有何区别.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


# id： 在内存中存储的位置
# type: 变量的；类型
# value： 值是否相等；
# == 判断： type， value
# is: type， value, id
# 结论:
#   is表示的是对象标识符;表示两个变量的值是否在同一块内存空间;
#   ==表示的是值是否相等;

# 总结: is返回值为True, ==返回一定是True;

"""


a = 'hello'
b = 'hello world'
print(a == b)


c = 18090
d = 18090
print(c==d)
print(id(c), id(d))





