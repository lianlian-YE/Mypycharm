#!/usr/bin/env python
#coding:utf-8


""""
Name: 01_通配符.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:



*:
?:
.:
..:

[[:digit:]]
[[:alpha:]]
[[:alnum:]]
[[:space:]]

"""


import glob

print(glob.glob('/etc/*.conf', recursive=True))
g = glob.iglob('/etc/*.conf')





