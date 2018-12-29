#!/usr/bin/env python
# coding:utf-8


""""
Name: 01_面向对象的第一个特性_封装.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

a = int(1)

li = list([1, 2, 3])


# # 定义函数
#
# def 函数名(形参):
#     pass
#
#
# # 执行函数， 必须要调用
# 返回结果  =  函数名(实参)



# # 定义类
# class 类名(父类名称):
#     pass
#
#
# # 执行类的内容， 也必须调用,这个过程称为实例化对象;
# 类名()




# 类，对象
# 属性： 类里面的变量，n
# 方法: 类里面的函数，v

# 类

#
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
# 对象
stu1 = Student("westos",10,100)
print(stu1)
print(stu1.name)
print(stu1.age)
print(stu1.score)
print(stu1.get_level())

# #
# stu2 = Student("王浪",18,90)
# print(stu2.name)
# print(stu2.age)
# print(stu2.score)