#!/usr/bin/env python
#coding:utf-8


""""
Name: 类的多继承算法.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:

# 经典类:
class 类名:
    pass


# 新式类
class 类名(父类):
    pass


"""


# 在python2中既有新式类也有经典类;
#       经典类的继承算法: 深度优先算法
#       新式类的继承算法: 广度优先算法


# python3全部都是新式类;

class D:
    pass
    # def test(self):
    #     print("D test")
class C(D):
    def test(self):
        print("C test")
class B(D):
    pass
    # def test(self):
    #     print("B test")
class A(B,C):
    pass
    # def test(self):
    #     print("A test")

a = A()
a.test()





