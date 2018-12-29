#!/usr/bin/env python
#coding:utf-8


""""
Name: 04_在 HTML 文本中添加图片.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""




import smtplib
from email.mime.image import MIMEImage
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
    # multipart/related类型除了可以携带各种附件外，
    # 还可以将其它内容以内嵌资源的方式存储在邮件中。
    # 比如我们在发送html格式的邮件内容时，可能使用图像作为html的背景;
    msg = MIMEMultipart()

    msg['From'] = sender
    ##############   如果要给多个用户发送邮件， 需要将列表连接成字符串;######################
    msg['To'] = "".join(receiver)
    msg['Subject'] = subject

    # multipart / alternative类型
    # 如果邮件中同时存在纯文本和超文本内容，则邮件需要在Content - Type
    # 域中定义multipart / alternative类型，
    # 邮件通过其boundary中的分段标识将纯文本、超文本和邮件的其它内容分成不同的段。
    msgAlter = MIMEMultipart()
    msg.attach( msgAlter)

    mail_msg = """
    <h1>hello</h1>
    <img src="cid:image"  alt="上海鲜花港 - 郁金香" />
    """


    msgAlter.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    with open('img/img01.jpg', 'rb') as f:
        msg_image = MIMEImage(f.read())

    msg_image.add_header('Content-ID','<image>' )
    msgAlter.attach(msg_image)
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


