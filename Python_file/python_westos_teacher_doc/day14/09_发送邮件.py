#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_发送邮件.py
Date: 2018/06/03
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



import smtplib
import getpass

passwd = getpass.getpass()
smtpObj = smtplib.SMTP('smtp.163.com')
print(smtpObj.ehlo())
print(smtpObj.starttls())
smtpObj.login('xc_guofan@163.com', passwd)
# smtpObj.sendmail('xc_guofan@163.com', '976131979@qq.com', 'Subject: a test mail\n Dear user: \n i\'m 163')
