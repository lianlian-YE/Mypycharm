#!/usr/bin/env python
#coding:utf-8


""""
Name: 19_迭代.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# iterable: 可迭代的; 可以for循环;


# s = "hello"
# # for(int i=0, i<length(s); i++)


s = 'hello'
for i in s:
    print(i)




#
from collections import Iterable

isinstance(1, int)
print(isinstance(1,Iterable))
print(isinstance({1,2,3},Iterable))






print(reversed([1,2,3,4]))
