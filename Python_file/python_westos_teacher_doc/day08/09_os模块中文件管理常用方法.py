#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_os模块中文件管理常用方法.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import os


# pwd=== print working directory
print(os.getcwd())

# ls
print(os.listdir('/var/log'))

#touch file
# 创建一个空文件;
# os.mknod('/tmp/westos')

# os.remove('/tmp/westos')

# os.mkdir('/tmp/westosdir')

## mkdir -p /tmp/ok/westosdir
# os.makedirs('/tmp/ok/westosdir')

## rm -fr  /tmp/ok/westosdir
# os.removedirs('/tmp/ok/westosdir')



print(os.path.isfile("/etc/passwd"))
print(os.path.isabs("~/passwd"))

# 判断文件或者目录是否存在;
print(os.path.exists('/etc/passwds'))
print(os.path.exists('/mnt'))


# Linux: /etc/passwd/hh
# Windows: C:\\book\python
print(os.path.split('/etc/passwd/hh'))

print(os.path.sep)   #\


# 获取文件名;
print(os.path.basename('/hello/hello.py'))
# 获取目录名
print(os.path.dirname('/hello/hello.py'))


print(os.path.splitext("hello.py"))
# mv
os.rename('/tmp/passwdok', '/mnt/passwdok')
