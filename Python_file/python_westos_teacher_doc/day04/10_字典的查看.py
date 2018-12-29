#!/usr/bin/env python
#coding:utf-8


""""
Name: 10_字典的查看.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

services = {
    "http":80,
    'ftp': 21,
    'ssh':22,
    'mysql':3306
}

# 查看字典的key值;
print(services.keys())

# 查看字典的value值;
print(services.values())

# 查看字典的(key,value)值;
print(services.items())



# 1. 查看key的value值；key不存在，则报错;
print(services['http'])
# print(services['https'])



# 2. 查看key的value值；
#       key不存在, 默认返回None；
#       key不存在， 有default值， 则返回default值;

print(services.get('http'))
print(services.get('https'))
print(services.get('https', 443))