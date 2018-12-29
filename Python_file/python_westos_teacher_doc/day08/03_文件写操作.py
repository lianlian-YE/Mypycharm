#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_文件写操作.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
# 1. 实现快速清空文件;
# f = open("/tmp/passwd", 'w')
# f.close()




# 2.
f = open("/tmp/passwd", 'a+')
li = ['user1', 'user2', 'user3']
# 文件写入时,也会移动指针,
f.write("hello")
f.writelines(['gcc\n', 'c++\n'])
f.writelines([line+"\n" for line in  li])
# 移动指针到文件最开始;
f.seek(0,0)
print(f.read())
f.close()













