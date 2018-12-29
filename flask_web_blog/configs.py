import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:yixin901213@localhost/flask_blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)
manager=Manager(app)
migrate=Migrate(app,db)
# mail=Mail(app)
manager.add_command('db',MigrateCommand)
bootstrap=Bootstrap(app)
app.secret_key='abcd'
loginmanager=LoginManager(app)
loginmanager.session_protection='strong'  #不同的安全等级防止会话遭到更改
loginmanager.login_view='auth.login'      #设置登录页面的端点

"""
集成电子邮件的功能 
"""
MAIL_SERVER = 'smtp.163.com'
MAIL_USERNAME='18829285068@163.com'
MAIL_PASSWORD='z901213'
MAIL_DEFAULT_SENDER='18829285068@163.com'
app.config['FLASKY_MAIL_SUBJECT_PREFIX']='[Flasky]'   #邮件主题前缀
app.config['FLASKY_MAIL_SENDER']='flasky admin <flasky@example.com>' #发送人地址
mail=Mail(app)
def send_email(to,subject,template,**kwargs):
    """
    电子邮件通用部分定义为函数
    :param to: 收件人地址
    :param subject: 主题
    :param template: 渲染模板
    :param kwargs: 关键字参数列表
    :return:
    """
    msg=Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,recipients=['1771764895@qq.com'])
    msg.body=render_template(template+'.txt',**kwargs)
    # msg.html=render_template(template+'.html',**kwargs)
    mail.send(msg)