#!/usr/bin/env python
#coding:utf-8


""""
Name: 05_封装数据库.py
Date: 2018/06/02
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

import config
import pymysql

class Mysql(object):
    def __init__(self, db_config):   # db_config dict
        # 在实例化对象时自动执行
        try:
            self.db_config = db_config
            self.conn = pymysql.connect(**self.db_config)  # (user='root')
            self.cur = self.conn.cursor()
        except Exception as e:
            print("连接数据库失败：", e)
        else:
            print("连接数据库成功!")


    def __str__(self):
        return  "Connect(%s user=%s db=%s)" %(
            self.db_config['host'], self.db_config['user'], self.db_config['db'])



    def __del__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()



test_sql = Mysql(config.db_config)
print(str(test_sql))