#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_类里面的魔术方法实现with语句的.py
Date: 2018/05/24
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


#
# with open('/etc/passwd') as f1, open('/etc/group') as f2:
#     print(f1.read(),f2.read())


import zipfile


class MyOpen(object):
    def __init__(self, filename, mode='r'):
        self.name = filename
        self.mode = mode

    def read(self):
        return self.f.read()

    def __enter__(self):
        self.f = open(self.name, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

with MyOpen('/etc/passwd') as f1, MyOpen('/etc/group') as f2:
    print(f1.read(), f2.read())


# with MyOpen('/etc/passwd') as f1, MyOpen("/etc/group") as f2:
#     print(f1.readline())
#     print(f2.readline())

# with open('/etc/passwd') as f1, open("/etc/group") as f2:
#     print(f1.readline())
#     print(f2.readline())



# with MyOpen("/etc/passwd") as f:
#     print(f.readline())
#     print(f.closed)
#
# print(f.closed)
#


# a = MyOpen('/etc/passwd')
#
# with a as f:
#     print("hello")







