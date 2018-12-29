#!/usr/bin/env python
#coding:utf-8


""""
Name: 06_生成器_迷你聊天机器人.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

def chat_robot():
    res = ''
    while True:
        receive = yield
        if 'age' in receive:
            res = "18"
        elif 'name' in receive:
            res = "小冰"
        elif 'hello' in receive:
            res = 'hello'
        else:
            res = "i dont know"
        print("Robot>>:%s" %(res))

def main():
    Robot = chat_robot()
    next(Robot)
    while True:
        send_data = input("A>>:")
        if send_data == 'q' or send_data == 'bye':
            print("不聊了")
            break
        Robot.send(send_data)


main()
