#!/usr/bin/env python
#coding:utf-8


""""
Name: 16_用户管理系统.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# 1. 用户信息怎么存?

# info['root']['passwd']
info = {
    'root':{
        "name":"root",
        "passwd":"redhat",
        "gender":1, # 1:男，2:女;
        "email": "root@qq.com",
        "age":18
    },
}




menu = """"

    1). 注册新用户
    2). 用户登录
    3). 注销用户
    4). 显示用户信息
    5). 退出系统(exit(0))

"""

# 函数：

def addUser():
    print("01-用户注册界面".center(20, '*'))
    inname = input("*注册用户名:").strip()
    # 判断用户是否已注册?
    if inname in info:
        print('Error:用户%s已注册!' % (inname))
    else:
        passwd = input("*密码:")
        gender = input("性别(1-男，2-女):")
        if not gender:
            gender = None
        else:
            gender = int(gender)
        email = input("邮箱地址:")
        if not email:
            email = None
        age = input("年龄:")
        if not age:
            age = None
        else:
            age = int(age)
        info[inname] = {
            "name": inname,
            "passwd": passwd,
            "gender": gender,  # 1:男，2:女;
            "email": email,
            "age": age
        }
        print("用户%s注册成功" % (inname))


def loginUser():
    tryCount = 0
    while tryCount < 3:
        tryCount += 1
        inuser = input("用户名:")
        # 1.判断用户是否存在？
        if inuser in info:
            # 2. 判断密码是否正确?
            inpasswd = input("密码:")
            # 找出系统存储的inuser用户的密码;
            passwd = info[inuser]['passwd']
            if inpasswd == passwd:
                print("%s登陆成功!" % (inuser))
                break
            else:
                print("用户%s的密码错误!" % (inuser))
        else:
            print("用户名%s不存在" % (inuser))
    else:
        print("尝试次数超过3次!")


def deleteUser():
    inuser = input("注销的用户名:")
    if inuser in info:
        del info[inuser]
        print("用户%s注销成功" % (inuser))
    else:
        print("用户名%s不存在" % (inuser))



def main():
    while True:
        print("用户登录系统".center(40, '*'), menu)
        choice = input("请输入你的选择:")
        if choice == '1':
            addUser()
        elif choice == '2':
            loginUser()
        elif choice == '3':
            deleteUser()
        elif choice == '4':
            print(info)
        elif choice == '5':
            exit(0)
        else:
            print("Error:错误输入!<请输入正确的选择.>")


main()