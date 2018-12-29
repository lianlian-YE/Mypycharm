#!/usr/bin/env python
#coding:utf-8


""""
Name: 04_with语句.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# # 当执行完with语句之后, 自动清理或者关闭文件对象;
# with open('/etc/passwd') as f:
#     print(f.closed)
#     print(f.read())
#
# print(f.closed)



# # 判断文件对象是否可迭代
# from collections import Iterable
#
# f = open("/etc/passwd")
# print(isinstance(f,Iterable))
#
# # 文件对象是可迭代,默认遍历文件的每一行;
# for line in f:
#     print(line)
