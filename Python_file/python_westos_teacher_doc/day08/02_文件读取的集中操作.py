#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_文件读取的集中操作.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# read
f = open("/tmp/passwd")
# f.read()
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())


# 批量删除文件内容列表信息的'\n'-----列表生成式
# print([line.strip() for line in f.readlines()])



# 读取文件指定个数个字节, 三个
print(f.read(3))
print(f.readline())

# seek方法, 移动指针
#   seek第一个参数是偏移量： >0， 代表向右移动, <0，代表向左移动
#   seek第2个参数是:
#       0:移动指针到文件开头
#       1: 不移动指针;
#       2:移动指针到文件末尾
f.seek(0,2)
# 查看指针当前位置
print(f.tell())
print(f.readable())





