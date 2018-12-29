#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_threading 模块创建线程.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import time
import threading



# 实现多线程的第一种方式:
# def song(name):
#     for i in range(5):
#         time.sleep(0.1)
#         print("正在听歌:%s" %(name))
#
# def code(name):
#     for i in range(5):
#         time.sleep(0.3)
#         print("正在编码:%s" %(name))
#
# song('hello')  # 15s
# code('hello')  # 10s
# t1 = threading.Thread(target=song, args=("sunshine",))
# t2 = threading.Thread(target=code, args=("python",))
# t1.start()
# t2.start()
#




## 2. 第2种实现多线程的方法:

class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        for i in range(5):
                time.sleep(0.3)
                print("正在", self.name )



# 声明线程为守护线程;
# 不设定守护线程时， 主线程执行结束， 不会结束子线程;
# 不设定守护线程时， 主线程执行结束， 子线程也结束;
#

t1 = MyThread("code")
t2 = MyThread("song")
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
t1.join()
t2.join()

print('end')
