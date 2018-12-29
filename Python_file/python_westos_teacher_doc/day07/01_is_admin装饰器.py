#!/usr/bin/env python
#coding:utf-8


""""
Name: 01_is_admin装饰器.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""




import functools
import inspect

def is_admin(fun):  # fun=add_student
    @functools.wraps(fun)
    def wrapper(*args, **kwargs): # kwargs = {'name':'root'}
        # inspect.getcallargs返回一个字典， key值为：形参， value值为对应的实参；
        inspect_res = inspect.getcallargs(fun, *args, **kwargs)
        print("inspect的返回值: %s" %(inspect_res))

        if inspect_res.get('name') == 'root':
            temp = fun(*args, **kwargs)
            return temp
        else:
            print("not root/admin user, no permisson add student")   # 抛出异常
    return wrapper


@is_admin   # add_student = is_admin(add_student)
def add_student(name):   #
    print("添加学生信息.....")
add_student('redhat')