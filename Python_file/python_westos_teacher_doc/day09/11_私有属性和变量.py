#!/usr/bin/env python
# coding:utf-8


""""
Name: 11_私有属性和变量.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 子类也不能直接使用父类的私有属性和私有方法;
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        # 以双下划线开头的属性名或者方法名， 外部是不可以访问的;
        self.__score = score
    def set_score(self, value):
        if 0<=value<=150:
            self.__score = value

    def __get_level(self):
        if 90<self.__score<=100:
            return "%s,%s,A" %(self.name,self.age)
        elif 80<self.__score<=90:
            return  "%s,%s,B" %(self.name,self.age)
        else:
            return  "%s,%s,C" %(self.name,self.age)




class MathStudent(Student):
    def get_score(self):
        print(self.__score)



s1 = Student("westos", 18, 100)
print(s1.name)

s2 = MathStudent("helo",10,90)
# print(s2.__score)
# s1.__get_level()
# print(s1.__score)
# s1.name = "fentiao"
# print(s1.name)
# s1.score = 150
# print(s1.score)