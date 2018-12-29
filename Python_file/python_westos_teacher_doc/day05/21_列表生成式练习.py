#!/usr/bin/env python
#coding:utf-8


""""
Name: 21_列表生成式练习.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


# 找出/var/log/目录中，所有以.log结尾的文件名或者目录名;
# os.listdir('/var/log/')
# if


"""
import os

print([filename for filename in os.listdir('/var/log') if filename.endswith('.log')])




# 2. 将列表中所有内容都变为小写；

li = ['frdgrfgdsHHJJ', 'cdsfregHHHJDGF']

print([i.lower() for i in li])