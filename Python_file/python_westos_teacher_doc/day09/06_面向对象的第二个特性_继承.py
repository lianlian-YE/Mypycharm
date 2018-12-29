#!/usr/bin/env python
#coding:utf-8


""""
Name: 06_面向对象的第二个特性_继承.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# 继承: 父类和子类; 基类和派生类.

class Student(object):
    # 类里面的变量名称为属性
    # name = "hello"
    # age = 15
    # score = 100
    # 构造函数， 实例化对象时，自动会执行的函数;
    def __init__(self, name, age, score):
        # self实际是实例化出来的对象
        # self.name把属性和对象进行绑定；
        self.name = name
        self.age = age
        self.score = score

        print("self:%s" %(self))

    # 在类里面定义的函数称为方法;
    # self参数， 是python解释器自动传递参数；
    def get_level(self):
        if 90<self.score<=100:
            return "%s,%s,A" %(self.name,self.age)
        elif 80<self.score<=90:
            return  "%s,%s,B" %(self.name,self.age)
        else:
            return  "%s,%s,C" %(self.name,self.age)



class SeniorStudent(Student):
    # 如果子类没有某个函数，则自动调用父类的函数;
    def __init__(self,name,age,score,gender):
        # 1.
        # self.name = name
        # self.age = age
        # self.score = score
        # 2.
        # Student.__init__(self,name,age,score)

        # 3.
        super(SeniorStudent, self).__init__(name,age,score)
        self.gender = gender

    def get_level(self):
        print("this is a senior score level")
        # return Student.get_level(self)
        return super(SeniorStudent, self).get_level()




s1 = SeniorStudent("westos",10,100, "男")
print(s1)
print(s1.get_level())

# self = Student("name", "age", "score")
# Student.__init__(self,"name", "age", "score")
#






