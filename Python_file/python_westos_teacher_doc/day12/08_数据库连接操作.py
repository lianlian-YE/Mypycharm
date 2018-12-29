#!/usr/bin/env python
# coding:utf-8


""""
Name: 08_数据库连接操作.py
Date: 2018/05/27
Connect: xc_guofan@163.com
Author: lvah
Desc:

# python2.7

"""

import MySQLdb

# ranom create user and passwd




# 1.# 创建与数据库的连接
conn = MySQLdb.connect(host='localhost',
                       user='root', passwd='westos',
                       db='hello', charset='utf8')

# 创建游标，给数据库发送sql语句/指令;
cur = conn.cursor()

users = [('user2', '123'), ('user3', '123'), ('user4', '123')]
try:
    cur.execute('create table userinfo(username varchar(10), passwd varchar(10));')
except Exception as e:
    print(e)

# cur.execute('insert into users values("user2", "123");')
# cur.execute('insert into userinfo values("user1", "123");')

# #
# for user, passwd in users:
#     insert_sqli = 'insert into userinfo values("%s", "%s");' %(user, passwd)
#     print('sql:'+insert_sqli)
#     cur.execute(insert_sqli)

insert_sqli = 'insert into userinfo values(%s, %s);'
cur.executemany(insert_sqli, users)
# 先关闭游标
cur.close()
# 对于数据库操作，一定要提交；
conn.commit()
# 关闭连接
conn.close()
