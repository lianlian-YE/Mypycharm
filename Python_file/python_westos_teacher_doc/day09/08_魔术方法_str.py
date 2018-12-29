#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_魔术方法_str.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        print("student is create")

    def __str__(self):
        return "Student:<%s,%s,%s>" %(self.name, self.age, self.score)
    def __del__(self):
        print("student is delete")
s1 = Student("westos", 19, 100)
print(s1)




