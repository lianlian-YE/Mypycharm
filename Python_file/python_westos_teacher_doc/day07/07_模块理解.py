#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_模块理解.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


import random
import hello



# 1. 内置模块的搜索路径查看;
import sys
# 列表
# print(sys.path)


for path in sys.path:
    print(path)


#2. 导入模块， 首先在当前路径寻找, 如果找不到去sys.path；
# 导入该模块的变量名和函数名........

print(hello.a)
print(hello.add(1,3))

#3. 添加路径到默认搜索路径中;
# sys.path.append('/root/Desktop/')
# sys.path.insert(0,'/root/Desktop')



#3. 模块分类
    # - 内置模块 ： random,sys,time,collections, functools, inspect
    # - 自定义模块: 自己写的模块;
    # - 第三方模块: pypi.python.org; itchat,qrcode




# 4.
#




