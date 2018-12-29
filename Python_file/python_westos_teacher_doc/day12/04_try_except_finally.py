#!/usr/bin/env python
#coding:utf-8


""""
Name: 04_try_except_finally.py
Date: 2018/05/27
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
try:
    f = open('/etc/passwd')
    # print(f1)
    f.read()
except  Exception as e:
    print(e)
else:
    print("all success")
finally:
    f.close()
print(f.closed)









try:
    with open('/etc/passwd') as f:
        # print(f1)
        f.read()
except  Exception as e:
    print(e)
else:
    print("all success")

print(f.closed)



