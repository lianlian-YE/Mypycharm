#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_gevent实现协程.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


# 1. gevent是一个第三方库， greenlet实现协程:
基本原理:
    当一个协程需要IO操作, （比如:访问网络, 读取硬盘的文件， 读取数据库内容）, 自动切换到其他协程
等到上一个IO操作结束后, 在适当的时候，切换回来继续执行.

# 2. 同步和异步：


"""
import time
from gevent import monkey
import threading
# 打补丁， 自动修改协程中需要的一些标准库;
monkey.patch_socket()


import gevent


def f(n):
    """协程需要处理的任务"""
    for i in range(n):
        print(gevent.getcurrent().name,threading.current_thread().name,  i)
        # 模拟IO操作
        # 通过gevent.sleep交出协程的控制权;
        gevent.sleep(1)
        

def Automain():
    # g1 = gevent.spawn(f, 5)
    # g2 = gevent.spawn(f, 5)
    # g3 = gevent.spawn(f, 5)
    #
    # g1.join()
    # g2.join()
    # g3.join()
    gevents = [gevent.spawn(f, 5) for i in range(3)]
    gevent.joinall(gevents)


from greenlet import greenlet

def task1():
    print('task1')
    gr2.switch()
    print('test1')
    gr2.switch()



def task2():
    print('test2')
    gr1.switch()
    print('test2')



# 人工切换协程， 比较麻烦， 建议使用gevent.spawn；
gr1 = greenlet(task1)
gr2 = greenlet(task2)
gr1.switch()










# Automain()
# 返回当前线程的名称;
# print(threading.current_thread().name)
