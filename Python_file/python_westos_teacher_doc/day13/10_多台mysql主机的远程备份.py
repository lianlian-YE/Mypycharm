#!/usr/bin/env python
# coding:utf-8


""""
Name: 10_多台mysql主机的远程备份.py
Date: 2018/06/02
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import os

import time

from mysqlInfo import mysql_list

BACKUP_DIR = '/mnt/BACKUP/'

if not os.path.exists(BACKUP_DIR):
    os.mkdir(BACKUP_DIR)
    print("%s create success!" % (BACKUP_DIR))
else:
    try:
        for host in mysql_list:
            # date = os.popen('date +%Y_%m_%d')
            shell_sen = "mysqldump -h %s -u%s -p%s %s >%s"
            host_ip = host['host']
            user = host['user']
            passwd = host['passwd']
            db = host['db']
            backup_filename = BACKUP_DIR + '%s_%s.dump' %(host_ip, db)
            print(backup_filename)
            print(shell_sen % (host_ip, user, passwd, db, backup_filename))
            os.system(shell_sen % (host_ip, user, passwd, db, backup_filename))
            print("backup %s host" %(host_ip))
    except Exception as e:
        print(e)
    else:
        print('sucess')
os.mknod(time.ctime())