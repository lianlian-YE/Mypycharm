#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_存储图片到数据库中.py
Date: 2018/06/02
Connect: xc_guofan@163.com
Author: lvah
Desc:

htt

https://imgsa.baidu.com/forum/w%3D580%3B/sign=a98b3f6f933df8dca63d8f99fd2a738b/0eb30f2442a7d93311d1d5eba14bd11373f00128.jpg

"""
import os

import  pymysql
from colorFont import *



# 1. 连接数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='westos', db='westos',
                       charset='utf8')

# 2. 创建游标， 给数据库发送sql指令
cur = conn.cursor()

# 3. 执行sql语句:

# 1). 创建存储图片的数据库表;
try:
    cur.execute('create table images('
                'id int primary key auto_increment , '
                'imgName varchar(50),'
                'imgData mediumblob); ')
except Exception as e:
    print(e)
else:
    print("table create sucess!")

# 2). 插入图片;
try:

    insert_sqli = 'insert into images (imgName, imgData) values(%s, %s);'
    f = open('img/img01.jpg', 'rb')
    img_data = f.read()
    f.close()
    cur.execute(insert_sqli, ('img01.jpg', img_data ))
except Exception as e:
    print(e)
else:
    print("插入图片信息成功!")

conn.commit()
# 4. 先关闭游标
cur.close()
# 5. 关闭数据库连接
conn.close()








