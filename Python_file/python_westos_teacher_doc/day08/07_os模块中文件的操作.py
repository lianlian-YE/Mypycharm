#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_os模块中文件的操作.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



import os



print(os.getcwd())

# os.remove('/tmp/passwd')

# os.removedirs('/tmp/hello')



print(os.path.splitext('hello.py'))
print(os.path.split('/home/aa/hello.py'))
print(os.path.dirname('/home/aa/hello.py'))
print(os.path.basename('/home/aa/hello.py'))

