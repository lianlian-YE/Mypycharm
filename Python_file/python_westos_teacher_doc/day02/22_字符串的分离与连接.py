#!/usr/bin/env python
#coding:utf-8


""""
Name: 22_字符串的分离与连接.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
s = '172.25.254.789'
# ['172', '25', '254', '789']列表数据类型
# split对于字符串进行分离， 分割符为"."
s1 = s.split(".")
print(s1[::-1])

date = '2018-04-22'
date1 = date.split("-")
# 倒序显示， 即反转;
date2 = date1[::-1]
print("date1:%s" %(date1))
print("date2:%s" %(date2))


# 连接, 通过指定的连接符， 连接每个字符串;
print("".join(date2))
print("/".join(date2))

print("/".join("hello"))
















