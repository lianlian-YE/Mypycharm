#!/usr/bin/env python
#coding:utf-8


""""
Name: oop理解.py
Date: 2018/06/10
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



class Process(object):
    def __init__(self, name=None, target=None):
        self.taeget = target
        self.name = name

class SubProcess(Process):
    def __init__(self,name, num):
        super(SubProcess, self).__init__(name=name)
        self.num = num

s= SubProcess("westos", 1)
print(s.name)






