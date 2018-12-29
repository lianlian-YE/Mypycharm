#!/usr/bin/env python
#coding:utf-8


""""
Name: mailConf.py
Date: 2018/06/09
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


import random

subjects = ['mail test', 'hello', 'text', 'world']


smtpServer = 'smtp.163.com'
sender = 'xc_guofan@163.com'
passwd = 'westos123'
# receiver = ['978661863@qq.com','liushaopeng3419@qq.com', '976131979@qq.com' ]
# receiver = '978661863@qq.com'
receiver = '976131979@qq.com'
subject = random.choice(subjects)


#
# with open("/etc/passwd") as f:
#     content = f.read()


with open('mail.html') as f:
    content = f.read()


