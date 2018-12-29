#!/usr/bin/env python
#coding:utf-8


""""
Name: 01_连接数据库.py
Date: 2018/06/02
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



import  pymysql
from colorFont import *

# 1. 连接数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='westos', db='westos',
                       charset='utf8')

# 2. 创建游标， 给数据库发送sql指令
cur = conn.cursor()

# 3. 执行sql语句
try:
    insert_sqli = 'insert into aa values("%s", "%s")' %('user23', '123')
    cur.execute(insert_sqli)
except Exception as e:
    print(FAIL + "sql execute failed:%s" %(insert_sqli) + END)
else:
    print(OKGREEN + "sql execute success:%s" %(insert_sqli) + END)
# 4. 提交sql语句， 作用于数据库;
conn.commit()

# 5. 先关闭游标
cur.close()
# 6. 关闭数据库连接
conn.close()
















