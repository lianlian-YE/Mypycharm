#!/usr/bin/env python
#coding:utf-8


""""
Name: 01_生成器的第2中实现方式.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
#
# # 生成器
#
# # 1. 列表生成式修改为生成器
#
#
# li = [i for i in range(100) if i%2==0]
# #  生成器
# g = (i for i in range(100) if i%2==0)
#
#
#
# # 2. 查看生成器内容的两种方式
#
#
# ## 2-1.python3中 g.__next__方法(), python2.x中g.next()；
# # python2.x, python3.x， next(g)
#
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
# #
# # print(next(g))
# #
#
#
#
# ## 2-2. for循环
# # isinstance(1, int)
# # isinstance(1, (int, float))
#
# from collections import Iterable
# print(isinstance(g, Iterable))
#
#
# #
# # for i in g:
# #     print(i)
#
#
#
# while True:
#     try:
#         print(g.__next__())
#     except StopIteration:
#         # print('end')
#         break







# __next__()
# send('xxxx')
# close()
# throw()



# g = (i**2 for i in range(5))
#
# print(g.__next__())
# # g.close()
# print(g.__next__())


def gen():
    while True:
        try:
            yield 'a'
        except TypeError:
            print('type error')


#  throw方法：给生成器发送一个异常(错误)； 但是不影响g.__next__()的执行;
#  close(): 关闭生成器， 再次执行g.__next__()报错;
g = gen()
print(g.__next__())
g.throw(TypeError)
print(g.__next__())




