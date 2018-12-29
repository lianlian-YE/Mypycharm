#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_itchat模块使用.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

import itchat
import random
import time
def main():
    info = [
        '新年快乐',
        '新春快乐',
        '新婚快乐',
        '2008快乐',
        '2009快乐',
        '2019快乐'
    ]
    itchat.auto_login()
    # for i in range(3):
    #     itchat.send(random.sample(info,1)[0], toUserName="filehelper")
    #     time.sleep(random.random())
    # itchat.send("hello python", toUserName="filehelper")
    # itchat.send_file('/etc/shadow',toUserName='filehelper')

    # for friend in itchat.get_friends()[1:]:
    #     itchat.send(friend['RemarkName']+random.sample(info,1)[0],toUserName=friend['UserName'])
    for i in itchat.get_chatrooms():
        print(i)

    # itchat.auto_login(hotReload=True)
    # info = itchat.get_friends()
    # # 1. 获取好友男女比例: 'Sex': 2:女; 1:男
    # male = female = other = 0
    # for friend in info[1:]:
    #     if friend['Sex'] == 1:
    #         male += 1
    #     elif friend['Sex'] == 2:
    #         female += 1
    #     else:
    #         other += 1
    # print("总好友个数:%d" %(len(info[1:])))
    # print("男性好友:%d" %(male))
    # print("女性好友:%d" %(female))
    # print("其他:%d" %(other))

if __name__ == "__main__":
    main()