#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_线程锁.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:

- 理解:
    - 对于进程, 进程之间资源不可以共享， (变量);
    - 对于线程, 一个进程中的所有线程共享资源（变量）;



- 什么时候加线程锁: 多个线程对同一个数据进行修改时；
"""
import threading
import time

money = 0
# 创建线程锁:
lock = threading.Lock()

def change_money(num):
    global  money
    money = money + num
    money = money - num


def sendMail():
    pass


def task():
    for i in range(1000000):
        # 获取创建的线程锁；
        lock.acquire()
        try:
            change_money(100)
        finally:
            # 释放线程锁;
            lock.release()
        sendMail()


#
# 没有使用多线程: ==0
# task()
# task()
# print(money)


## 使用多进程
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start()
t2.start()
# 等待所有子线程执行结束，再执行主线程;
t1.join()
t2.join()
print("当前金额:", money)


