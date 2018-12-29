#!/usr/bin/env python
#coding:utf-8


""""
Name: 01_协程.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:




进程:
线程:
协程:又称为微线程(coroutine);yield

import gevent
"""




def A():
    print('1')
    print('2')
    print('3')


def B():
    print('x')
    print('y')
    print('z')



# 协程在执行时， 可以随时中断, 有点像多线程;
# 协程始终只有一个线程在执行;




# 1. 协程的优势:
#       1). 协程没有切换线程时的开销， 是由程序自身来控制, 执行效率高;
#       2). 协程控制资源时， 不需要加锁；

# 2. 协程的实现方式:
#       1). yield关键字;






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
    # Robot
    Robot = chat_robot()
    next(Robot)
    while True:
        send_data = input("A>>:")
        if send_data == 'q' or send_data == 'bye':
            print("不聊了")
            break
        Robot.send(send_data)


main()
