#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_Python发送HTML格式的邮件.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""





import smtplib
from email.mime.text import MIMEText

from mailConf import *

def mail_content():
    # 是一个MIMETEXT对象, 如果发送的是普通的文本文件， 则添加
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = sender
    ##############   如果要给多个用户发送邮件， 需要将列表连接成字符串;######################
    msg['To'] = "".join(receiver)
    msg['Subject'] = subject
    return  msg

def sendMail():
    try:
        # 1. 连接smtp服务器;
        smtpObj = smtplib.SMTP(smtpServer)
        # 2. 登陆账户
        smtpObj.login(sender, passwd)
        # 生成合法格式的内容， 否则发送失败;
        msg = mail_content()
        # 3. 发送邮件
        smtpObj.sendmail(sender, receiver, msg.as_string())
    except smtplib.SMTPException as e:
        print("Error:邮件发送失败,",e)
    else:
        print("邮件发送%s成功" %(receiver))

if __name__ == "__main__":
    sendMail()

