#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_字典的增加.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


services = {
    "http":80,
    'ftp': 21,
    'ssh':22
}


# # 1. 增加一个元素;
#   1). 如果key值存在， 则更新对应的value值;
#   2). 如果key值不存在， 则添加对应的key-value值
# services['mysql'] = 3306
# print(services)
#
# services['http'] = 443
# print(services)




# 2. 添加多个key-value值；
#   1). 如果key值存在， 则更新对应的value值;
#   2). 如果key值不存在， 则添加对应的key-value值
# service_backup = {
#     'https':443,
#     'tomcat':8080,
#     'http':8080
#
# }
# services.update(service_backup)
# print(services)



# services.update(flask=9000, http=8080)
# print(services)







print(services)

# 3.setdefault添加key值;
#   1). 如果key值存在， 则不做修改;
#   2). 如果key值不存在， 则添加对应的key-value值
services.setdefault('http',9090)
print(services)

services.setdefault('oracle',44575)
print(services)


