#!/usr/bin/env python
# coding:utf-8


""""
Name: 16_参数检测.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:



# 参数检测
isinstance(1, int)
True
isinstance(1.0, float)
True
isinstance(2+3j, float)
False
isinstance(2+3j, tuple)
False
isinstance(1, (int, float, long, complex))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'long' is not defined
isinstance(1, (int, float,complex))
True


"""


def add(x:int, y:int)->int:
    """
    add: sum x and y

    :param x: int,float,.....
    :param y: int,float.....
    :return: int
    """
    if isinstance(x,(int,float,complex)) and isinstance(y,(int,float,complex)):
        return x + y
    else:
        print("Error")

#
# res = add("hello", 2)
# print(res)
help(add)


# *args, **kwargs




#

def fun(d=2, c=3):
    pass