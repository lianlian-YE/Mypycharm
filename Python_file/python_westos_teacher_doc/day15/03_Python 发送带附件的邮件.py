#!/usr/bin/env python
# coding:utf-8


""""
Name: 03_Python 发送带附件的邮件.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:



发送带附件的邮件，首先要创建MIMEMultipart()实例，
然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mailConf import *


def read_file(filename):
    """读取附件文件的内容"""
    with open(filename, 'rb') as f:
        c_str = f.read()
    return c_str


def mail_content():
    # 创佳一个 MIMEMultipart对象， 可以添加很多内容, 比如附件
    # **************此处修改MIMEMultipart()实例可以添加附件**************
    msg = MIMEMultipart()

    msg['From'] = sender
    ##############   如果要给多个用户发送邮件， 需要将列表连接成字符串;######################
    msg['To'] = "".join(receiver)
    msg['Subject'] = subject


    # 添加邮件正文
    msg.attach(MIMEText("这是一个有附件的邮件正文."))

    # 构造邮件的附件
    att1_content = read_file('/etc/passwd')
    # 构建附件1：
    # Base64是网络上最常见的用于传输8Bit字节码的编码方式之一，
    # Base64就是一种基于64个可打印字符来表示二进制数据的方法。
    att1 = MIMEText(att1_content, 'base64', 'utf-8')

    # Content-Type，内容类型，一般是指网页中存在的Content-Type，
    # 用于定义网络文件的类型和网页的编码，决定浏览器将以什么形式、什么编码读取这个文件，
    # 这就是经常看到一些Asp网页点击的结果却是下载到的一个文件或一张图片的原因。
    # 'application/octet-stream': .* （ 二进制流，不知道下载文件类型）
    att1['Content-type'] = 'application/octet-stream'

    # HTTP应答中，Content-Disposition 消息头指示回复的内容该以何种形式展示，
    # 是以内联的形式（即网页或者页面的一部分），还是以附件的形式下载并保存到本地
    #
    # inline（默认值，表示回复中的消息体会以页面的一部分或者整个页面的形式展示），
    # attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，
    #   将filename的值预填为下载后的文件

    att1['Content-Disposition'] = "attachment; filename='westos'"
    msg.attach(att1)
    return msg


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
        print("Error:邮件发送失败,", e)
    else:
        print("邮件发送%s成功" % (receiver))


if __name__ == "__main__":
    sendMail()
