#!/usr/bin/env python
# coding:utf-8


""""
Name: 06_字典的特性.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:




# 索引， 切片， 重复， 连接，成员操作符, for



# set不支持 索引， 切片， 重复， 连接，， 因为set是无序的；
"""

# 1. 判断字典是否是无序的?
# python2中字典加入顺序和存储顺序不一致；
# python3中字典加入顺序和存储顺序一致；

d = {
    '1': 'a',
    '8': 'b'

}

# print(d['1'])

# 字典是不支持索引的；
# print(d[0])

# 字典是不支持切片的；
# print(d[::])


# 字典的重复和连接无意义, 字典的key值是唯一的;
# print(d*3)



# 成员操作符;判断的是某个值是否为字典的key；
# print('1' in d)
# print('1' not in d)


# 字典for循环时， 默认遍历字典的key值;
for key in d:
    print(key)


# 遍历字典:
for key in d:
    print(key, d[key])