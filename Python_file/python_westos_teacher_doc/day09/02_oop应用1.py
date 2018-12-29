#!/usr/bin/env python
# coding:utf-8


""""
Name: 02_oop应用1.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


class People(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def goHome(self):
        print("%s,%s岁，%s, 辍学回家" % (
            self.name, self.age, self.gender))

    def kanChai(self):
        print("%s,%s岁，%s,上山砍柴" % (
            self.name, self.age, self.gender))

    def quXiFu(self):
        print("%s,%s岁，%s, 开车。。。。。。" % (
            self.name, self.age, self.gender))


# p1 = People("老李", 18, '男')
# p1.quXiFu()









