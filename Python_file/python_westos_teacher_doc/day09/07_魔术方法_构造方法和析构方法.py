#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_魔术方法_构造方法和析构方法.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# class Student(object):
#     def __init__(self):
#         print("student is create")
#     def __del__(self):
#         print("student is delete")
# s1 = Student()
# del s1



class OpenFile(object):
    def __init__(self, filename, mode):
        print("file is opening.......")
        self.f = open(filename, mode)
    def closed(self):
        return  self.f.closed
    def __del__(self):
        # del f1
        # 程序执行结束....
        self.f.close()
        print("file is deleteing.....", self.f.closed)


f = OpenFile('/etc/passwd', 'r')
print(f.closed())

# del f
# print(f.closed())