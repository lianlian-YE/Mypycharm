#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_使用with安全上下文管理器.py
Date: 2018/06/02
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



# f = open('/etc/passwd')
# f.read()
# f.close()



# with open('/etc/passwd') as f:
#     f.read()



import pymysql




# 1. 连接数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='westos', db='westos',
                       charset='utf8')

with conn:
    cur = conn.cursor()