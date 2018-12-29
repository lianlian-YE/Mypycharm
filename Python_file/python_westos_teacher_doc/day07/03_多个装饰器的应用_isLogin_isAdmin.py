#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_多个装饰器的应用_isLogin_isAdmin.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



# 总结：在实际的应用场景中，会采用多个装饰器先验证是否登陆成功，再验证权限是否足够;





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
            print("Error:not root/admin user, no permisson add student")   # 抛出异常
    return wrapper



login_seesion = ['root', 'admin', 'redhat']

def is_login(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        if args[0] in login_seesion:
            temp = fun(*args, **kwargs)
            return temp
        else:
            print("Error: %s未登陆!" %(args[0]))
    return wrapper

@is_login
@is_admin  # is_admin()
def add_student(name):
    print("添加学生信息.....")
add_student('aa')