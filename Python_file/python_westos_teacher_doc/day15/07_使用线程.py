#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_使用线程.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import time
import _thread



def song(name):
    for i in range(5):
        time.sleep(3)
        print("正在听歌")

def code(name):
    for i in range(5):
        time.sleep(2)
        print("正在编码")

# 这两个工作肯定是一个执行结束， 另外一个任务才开始执行;
# song()
# code()

_thread.start_new_thread(song, ('song',))
_thread.start_new_thread(code, ('code',))

while 1:
    pass





# def work(name):
#     for i in range(5):
#         time.sleep(0.5)
#         print("%s:%s"  %(name, time.ctime()))
#
#
# # 创建两个线程
# try:
#     _thread.start_new_thread(work, ('thread-1',))
#     _thread.start_new_thread(work, ('thread-2',))
# except Exception as e:
#     print(e)
#
#
# while 1:
#     pass
