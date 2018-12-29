#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_反射.py
Date: 2018/05/20
Connect: xc_guofan@163.com
Author: lvah
Desc:


有时候我们会碰到这样的需求，需要执行对象的某个方法，
或是需要对对象的某个字段赋值，而方法名或是字段名在
编码代码时并不能确定，需要通过参数传递字符串的形式输入。

这个机制被称为反射或是自省（反过来让对象告诉我们他是什么）;



1. 访问对象的属性
#
dir([obj]):
hasattr(obj, attr):
getattr(obj, attr):
setattr(obj, attr, val):



2. 确定对象的类型
isinstance(object, classinfo):




"""


class MyOpen(object):
    """this is a like open function"""
    def __init__(self, filename, mode='r'):
        self.name = filename
        self.mode = mode


    def get_name(self):
        a = 2
        print("get name info name......", end=' ')
        return self.name

    def get_mode(self):
        return self.mode



open1 = MyOpen('/etc/passwd')
open2 = MyOpen('/etc/passwd')
# print(open1)
# print(open1.__class__)
# print(open1.__dict__)
# print(open1.__doc__)


# # __eq__
# print(open1 == open2)


# 这个对象可以查看的属性或者可以执行的方法, 魔术方法;
print(dir(open1))

#
#
# # hasattr: 判断对象是否包含对应的属性或者方法名;
# print(hasattr(open1, 'name'))
# print(hasattr(open1, 'mode'))
# print(hasattr(open1, 'get_name'))
# print(hasattr(open1, 'set_name'))
# print(hasattr(open1, '__eq__'))
# #
#
#
# # getattr()用于返回对象的属性值;
#
#
# print(getattr(open1, 'name'))

#
# if hasattr(open1, 'name1'):
#     print(getattr(open1, 'name1'))
# else:
#     print("no name1 property")


# # 如果open1对象没有name1属性， 则默认返回westos； 如果没有提供默认值，则直接报错.
# print(getattr(open1, 'name1', 'westos'))
#
# # 获取open1对象的get_name方法， 返回的是函数对象， 如果要运行， 必须要调用;
# fun = getattr(open1, 'get_name')
# print(fun())
# #
#
# # setattr：用来设置属性值;
# setattr(open1, 'name', '/etc/group')
# print("修改后的文件名为: ",  getattr(open1, 'name'))
#
#
# setattr(open1, 'westos', '11')
# print(hasattr(open1, 'westos'))
# print(getattr(open1, 'westos'))
# #
# #
#
#
# # setattr：用来设方法;
def aa():
    return "this is add functions"

# 执行MyOpen类里面的get_name;
# print(getattr(open1, 'get_name')())
setattr(open1, 'get_name', aa)
print(getattr(open1, 'get_name')())
print(getattr(open2, 'get_name')())
# #
# l = list([])
# print(isinstance(l, list))
# print(isinstance(open1, (MyOpen, list)))