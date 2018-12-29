#!/usr/bin/env python
#coding:utf-8


""""
Name: 06_获取单个表的字段名和信息.py
Date: 2018/06/02
Connect: xc_guofan@163.com
Author: lvah
Desc:


rows = cur.fetchall()

desc = cur.description
print("cur的描述信息:", desc)
print(" ".join([i[0] for i in desc]))


"""


import  pymysql
from colorFont import *



# 1. 连接数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='westos', db='westos',
                       charset='utf8')

# 2. 创建游标， 给数据库发送sql指令
cur = conn.cursor()

# 3. 执行sql语句: 查看数据
res = cur.execute('select * from aa;')
desc = cur.description
print("表的描述信息:", desc)

table_header = [item[0] for item in desc]
print("表头:", table_header)

print("\t".join(table_header))
for row in cur.fetchall():
    print("\t".join(row))



# 4. 先关闭游标
cur.close()
# 5. 关闭数据库连接
conn.close()









