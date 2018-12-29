#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_yield理解.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""




# 1. 当在函数中看到yield关键字， 那么这个函数调用的返回值是一个生成器;
# 2. 当要执行函数fun时， 必须调用g.__next__();
# 3. 函数执行时， 直到遇到yield停止;
# 4. 想要继续执行， 调用g.__next__();从上一次停止的地方继续执行;
def fun():
    a = "world"
    print("hello")
    print(1)
    yield 2
    print(3)
    yield 4

g = fun()
print(g)

for i in g:    # g.__next__()
    print(i)





# g.__next__()
# g.__next__()



# print(g.__next__())
# print(g.__next__())