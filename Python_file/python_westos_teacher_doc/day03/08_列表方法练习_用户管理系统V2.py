#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_列表方法练习_用户管理系统V2.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


用户登陆系统Version2：
	    1). 已知多个用户名和密码分别保存在列表中;
	    2). 判断用户名是否存在，
	            如果登陆的用户不存在，则报错;；
	            如果用户存在， 则判断密码是否正确：
                    如果正确， 输出用户登陆成功;
                    如果不正确， 输出登陆失败;

        3). 为防止黑客暴力破解密码， 登陆最多有3次机会;
"""
names = ['root', 'student']
passwds = ['redhat', 'student']

tryCount = 0
while tryCount < 3:
    tryCount += 1
    inuser = input("用户名:")
    # 1.判断用户是否存在？
    if inuser in names:
        # 2. 判断密码是否正确?
        inpasswd = input("密码:")
        # 找出系统存储的inuser用户的密码;
        index = names.index(inuser)   # inuser='root', index=0
        passwd = passwds[index]     # passwd='redhat'
        if inpasswd == passwd:
            print("%s登陆成功!" %(inuser))
            break
    else:
        print("用户名%s不存在" %(inuser))
else:
    print("尝试次数超过3次!")