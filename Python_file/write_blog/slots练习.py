from types import MethodType
class Student(object):
    def __init__(self,sex):
        self.sex=sex
    __slots__ = ['name','age','score']

s=Student('f')
# print(s.sex)
# def set_age(self,age):
#     self.age=age
# s=Student()
# s2=Student()
# s.name='xinxin'
# Student.set_age=set_age
# s.set_age=MethodType(set_age,s)
# s.set_age(5)
# s2.set_age(10)
# print(s.name)
# print(s.age)
# print(s2.age)