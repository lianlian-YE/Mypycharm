#!/usr/bin/env python
# coding:utf-8


""""
Name: 03_队列数据结构的封装.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import random


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop(0)

    def head(self):
        if not self.isEmpty():
            return self.queue[0]

    def tail(self):
        if not self.isEmpty():
            return self.queue[-1]

    def length(self):
        return len(self.queue)

    def isEmpty(self):
        # return self.queue == []
        return len(self.queue) == 0

    def view(self):
        if not self.isEmpty():
            for i in self.queue:
                print(i, end=",")
q1 = Queue()

for i in range(5):
    q1.enqueue(random.randint(1,10))


q1.view()



