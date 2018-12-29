#!/usr/bin/env python
# coding:utf-8


""""
Name: 22_集合数据类型.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 集合元素是不可重复的；
s = {1, 2, 3, 1, 2, 3}
print(s)


# 列表去重;
names = ['hello', 'world', 'hello']
print(list(set(names)))


# 集合的特性： (索引， 切片， 重复， 连接，)===> 不支持， 因为无序;  成员操作符， for循环 ===> 支持;

# 集合是无序的数据类型: 添加元素的顺序和存储的顺序无关;
"""
s = {2,5,8,20}
s
{8, 2, 20, 5}
s.add(6)
s
{2, 5, 6, 8, 20}

"""
# print(s[0])
# print(s[1:])
# print(s*3)

# print(s + {6,7,8})


print(1 in s)

for i  in s:
    print(i, end='')



