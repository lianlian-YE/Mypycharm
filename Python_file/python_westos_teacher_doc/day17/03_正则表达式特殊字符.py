#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_正则表达式特殊字符.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:



\d:digit代表单个数字 ======= [[:digit:]]
\D:单个非数字
\s:space代表空格（\n, \t,\r, ' '） ======= [[:space:]]
\S:
\w:word, 代表单个字母， 数字或者下划线  ==== [[:alnum:]] and '_'
\W:
.: 代表任意单个字符;
"""



import re


# pattern = r""
# s = ""
# re.findall(pattern, s)


print(re.findall(r'\d', '阅读人数为100'))
print(re.findall(r'\D', '阅读人数为100'))
print(re.findall(r'\s', '\t阅读人数为100\n\r '))
print(re.findall(r'\S', '\t阅读人数为100\n\r '))
print(re.findall(r'\w', 'root email: he_llo@163.com'))
print(re.findall(r'\W', 'root email: he_llo@163.com'))

