import random

import redis
import time
from flask import Flask
'''
功能：可以看到用户在线的好友列表
分析：在线好友=全站在线用户集合和某个用户所有好友集合的交集。——基本数据类型：集合
问题：如何判断用户是否在线？
方案1：记录用户发送http请求的时间，指定时间内发送过请求的用户即为在线用户。
——每隔十分钟，用一个建来接收十分钟内发送过请求的用户ID列表。获取当前用户只需读取当前分钟对应的建即可。
————10：20~10:29访问者id存储在active.users:2中，10:30~10:39访问者id存储在active.users:3中。
————当用户10:29访问时，一分钟后即过期。存在误差。
方案进阶：每一分钟，接收一次用户ID列表。
——判断最近十分钟在线——判断在最近的十个集合键中是否出现过至少一次。sunion命令可实现

'''
r=redis.StrictRedis()
app=Flask(__name__)

@app.route('/')
def visit():
    """
    访问函数。模拟用户访问
    :return:
    """
    user_id=random.randint(1,100)
    current_key='active.users:'+time.strftime('%M',time.localtime(time.time())) #返回当前时间对应的建名
    pipe=r.pipeline()
    pipe.sadd(current_key,user_id)
    pipe.expire(current_key,10*60) #设置键的生存时间为10分钟
    pipe.execute()
    return 'user:%s \nkey:%s'%(user_id,current_key)
@app.route('/online/')
def online():
    """
    查看当前在线的用户列表
    :return:
    """
    result=[]          #存储近十分钟的键名
    for i in range(10):
        result.append('active.users:'+time.strftime('%M',time.localtime(time.time()-i*60)))
    online_user=r.sunion(result)
    online_result=''
    for user in online_user:
        online_result+='user: %s'%user
    return online_result

if __name__=='__main__':
    app.run()