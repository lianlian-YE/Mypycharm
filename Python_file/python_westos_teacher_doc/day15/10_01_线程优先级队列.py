#!/usr/bin/env python
# coding:utf-8


""""
Name: 10_线程优先级队列.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:





1. 什么是生产者消费者模型?

# 生产者
def allfile(dirname):
    pass
# 队列:
queue = []
# 消费者
def rename(filelist):
    pass


2. 生产者-消费者模型的优势：
1) : 解耦
2). 并发
3). 支持忙闲不均



"""
import os
import random
import threading

import time
from queue import Queue


class Producer(threading.Thread):
    def __init__(self, dirname, queue):
        # 继承父类的构造函数;
        super(Producer, self).__init__()
        self.dirname = dirname
        self.queue = queue

    def run(self):
        # 判断队列是否满?
        all_files = []
        for root, dir, files in os.walk(self.dirname):
            for file in files:
                all_files.append(os.path.join(root, file))
        print(all_files)

        for file in all_files:
            if self.queue.full():
                print("queue is full, producder wait!")
            else:
                self.queue.put(file)
                print("%s put %s into queue" % (self.name, file))


class Consumer(threading.Thread):
    def __init__(self,  queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        # 判断队列是否为空;
        if self.queue.empty():
            print("queue is empty, consumer wait!")
        else:
            # 从队列中拿出数据， 进行操作, 队列中该数据删除;
            value = self.queue.get()
            with open(value) as f:
                line = len(f.readlines())
                print("%s行数:%d" %(value, line))
            print("队列中还有%s个任务需要执行!" % (self.queue.qsize()))

# 创建一个队列的对象;
q = Queue(100)

threads = []

dirnames = ['/etc']


for dir in dirnames:
    threads.append(Producer(dir, q))


threads.append(Consumer(q))

for mythread in threads:
    mythread.start()

for mythread in threads:
    mythread.join()

print("执行结束!")
