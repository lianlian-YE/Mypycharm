#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_字典的删除.py
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
# 1.
# del services['http']
# print(services)


# 2. pop删除指定key的key-value对,
#   1). 如果key存在, 删除， 并且返回删除key对应的value值;
#   2). 如果key不存在, 直接报错
# item = services.pop('http')
# print(item)
# print(services)


# item = services.pop('https')
# print(item)
# print(services)


#3. popitem删除最后一个key-value值;
item = services.popitem()
print("删除的key-value对是:", item)
print(services)


# 4. 清空字典内容;
services.clear()
print(services)