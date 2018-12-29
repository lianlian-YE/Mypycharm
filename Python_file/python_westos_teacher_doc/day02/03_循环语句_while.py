#!/usr/bin/env python
# coding:utf-8


""""
Name: 03_循环语句_while.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


while 条件表达式:
    pass

"""

# count = 0
# while count < 5:
#     print("hello world")
#     count += 1  # count = count + 1





# 2. 循环语句的第二个问题: 如何跳出循环?
# break:
# continue:
import getpass

tryCount = 0
while tryCount < 3:
    username = input('用户名:')
    # passwd = input('密码:')
    passwd = getpass.getpass("密码:")
    if username == 'root' and passwd == 'redhat':
        print('login ok')
        break
    tryCount += 1
