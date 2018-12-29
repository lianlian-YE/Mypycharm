#!/usr/bin/env python
#coding:utf-8


""""
Name: 04_生产者消费者模型.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:

shop                    consumer
"""


import time
import random


def consumer(name):
    print("%s准备买包子....." %(name))
    while True:
        kind = yield
        print("%s已经购买%s口味包子....." %(name, kind))


# g = consumer("王东")
# g.__next__()
# # send方法， 给生成器传递值， 直到遇到下一个yield停止;
# g.send("特辣")



def producer(name):
    c1 = consumer("王东")
    c2 = consumer("王旭")
    c1.__next__()
    c2.__next__()
    print(c1 is c2)

    print("厨师%s准备制作包子......" %(name))
    for kind in ['特辣', '微辣','三鲜']:
        time.sleep(random.random())
        print("%s制作了%s口味的包子" %(name, kind))
        c1.send(kind)
        c2.send(kind)

producer('张玉娥')










