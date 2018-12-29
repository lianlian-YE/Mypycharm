#!/usr/bin/env python
# coding:utf-8


""""
Name: 23_集合生成式.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

print({i ** 2 for i in {1, 2, 3}})
print({i ** 2 for i in {1, 2, 3, 9, 12} if i % 3 == 0})
