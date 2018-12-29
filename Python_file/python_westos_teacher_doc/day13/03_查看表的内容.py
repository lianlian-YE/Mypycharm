#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_查看表的内容.py
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

# 3. 执行sql语句: 查看数据
res = cur.execute('select * from aa;')


# 每次查看表中的一条数据;
print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())

#
#
# # 如何移动游标;relative: 相对的， 相对当前游标向前还是向后移动;
# # 'absolute'默认移动到最开始;
# # cur.scroll(2,'relative')
# cur.scroll(5, 'absolute')
# print(cur.fetchone())

# 查看指定条表的内容, 元组里面嵌套元组;
# print(cur.fetchmany(5))
# 显示所有数据
# print(cur.fetchall())
# 依次将数据保存到文件中;
# try:
#     with open('/tmp/users.txt', 'w') as f:
#         for userinfo in cur.fetchall():   # userinfo=('name', 'passwd')
#             info = ":".join(userinfo)
#             f.write(info+'\n')
#
# except Exception as e:
#     pass
# else:
#     pass





# 4. 先关闭游标
cur.close()
# 5. 关闭数据库连接
conn.close()





