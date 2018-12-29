#!/usr/bin/env python
#coding:utf-8


""""
Name: 16_装饰器第2个模板.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import functools


def is_admin(fun):  # fun=add_student
    @functools.wraps(fun)
    def wrapper(*args, **kwargs): # kwargs = {'name':'root'}
        if kwargs.get('name') == 'root':
            temp = fun(*args, **kwargs)
            return temp
        else:
            print("not root/admin user, no permisson add student")
    return wrapper


@is_admin   # add_student = is_admin(add_student)
def add_student(name):
    print("添加学生信息.....")
add_student(name='root')