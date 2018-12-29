#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_批量插入多条数据.py
Date: 2018/06/02
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



import  pymysql
from colorFont import *

def create_user_data(n):  # 100
    users = []
    for i in range(n):   # 0，1，2，3，
        username = 'user'+str(i+1)
        users.append((username, '000000'))
    return users



# print(create_user_data(100))



# 1. 连接数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='westos', db='westos',
                       charset='utf8')

# 2. 创建游标， 给数据库发送sql指令
cur = conn.cursor()

# 3. 执行sql语句: 插入多条数据

try:
    # 执行的插入语句；
    insert_sqli = 'insert into aa values(%s,%s)'
    # 执行函数， 随机生成n条用户数据; 列表里面嵌套元组; [('user1', '000000'), ('user2', '00000')]
    users = create_user_data(90)
    # 'insert into aa values(%s,%s)' %('user1', '000000')
    # 'insert into aa values(%s,%s)' %('user2', '00000')]
    cur.executemany(insert_sqli, users)



except Exception as e:
    print(FAIL + "sql execute failed"+ END)
else:
    print(OKGREEN + "sql execute success" + END)


# 4. 提交sql语句， 作用于数据库;
conn.commit()

# 5. 先关闭游标
cur.close()
# 6. 关闭数据库连接
conn.close()







