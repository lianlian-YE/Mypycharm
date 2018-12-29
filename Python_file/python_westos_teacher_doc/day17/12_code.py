#!/usr/bin/env python
#coding:utf-8


""""
Name: 12_code.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import re
#
# pattern = r'westos'
# s = "qq westos world westos"
# matchObj = re.search(pattern, s)
# matchObj1 = re.match(pattern, s)
# if matchObj1:
#     print(matchObj1.group())
#



#
# s = "阅读次数为10000, 转发次数为100"
# # print(re.sub(r'\d+', '0', s))
#
#
# # 需求: 对于匹配到的内容全部加1：
# def addOne(matchObj):
#     """matchObj是匹配到内容的Match对象"""
#     res = int(matchObj.group()) + 1
#     return str(res)
# print(re.sub(r'\d+', addOne, s))

#
# pattern = r'=|\+|-|\*|/'
# print(re.split(pattern, '12+18-89/67*7=67'))




import re
# search函数在任意位置匹配符合正则表达式的内容;
# match方法从字符串的起始位置对模式进行匹配
pattern = r'http://(.+)'
s = "http://hello.com hello  \t world http://www.baidu.com   \thttp://www.qq.com"
print(re.search(pattern, s))
print(re.match(pattern, s))


# pattern = r'westos'
# s  = 'westos hello westos qq westos'
# print(re.search(pattern, s))



