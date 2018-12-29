#!/usr/bin/env python
#coding:utf-8


""""
Name: 05_while死循环.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 1. 死循环的几种写法
# while True:
#     print('hello')
#
#
# while 0<1:
#     print("hello")
#
#
# while 1:
#     print("hello")



# 2.continue和break的区别

while True:
    cmd = input('Command:')
    if not cmd:
        continue
    elif cmd == 'q':
        break
    else:
        print('execute cmd %s' %(cmd))



# if "hello":
#     print("hello")
# else:
#     print("not hello")


# 3. if和while后面必须跟的是bool类型， 如果不是布尔类型，转化为bool类型
# print(bool("hello"))   # True
# print(bool(""))       # False