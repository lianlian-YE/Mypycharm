#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_探究多个装饰器的执行顺序.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""



def decorator_a(func):
    print('Get in decorator_a')
    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a

def decorator_b(func):
    print('Get in decorator_b')
    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b



# 当有多个装饰器时， 从下到上调用装饰器；
@decorator_b   #  f =  decorator_b(inner_a)   # f = inner_b
@decorator_a   # f = decorator_a(f)    # f = inner_a
def f(x):
    print('Get in f')
    return x * 2

f(1)   # inner_b(1)





# 总结：在实际的应用场景中，会采用多个装饰器先验证是否登陆成功，再验证权限是否足够(is_admin);


