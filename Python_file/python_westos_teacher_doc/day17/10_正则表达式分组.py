#!/usr/bin/env python
#coding:utf-8


""""
Name: 10_正则表达式分组.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:

表示分组:


***1.
    (\d+)
    (.*)
    (\w+)

    # 当规则为pattern = r'<a href="/p/.*?pn=(.*)">尾页</a>',
    # 执行re.findall(pattern, content)时， 匹配的不是所有内容, 而是()里面/分组里面匹配到的内容;



**2.
    (\d+|\w+): 左右任意一个表达式满足即可


**3.\num

   \1, \2

** 分组起别名；
    (?P<name>)

"""




# 1. 在一个文档中匹配所有的IP地址;
# ********************子表达式重复出现多少次, 通过分组来实现****************************
# 172.12.1.1
#
# import re
# with open('ip.txt') as f:
#     content = f.read()
# # pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# pattern = r'((\d{1,3}\.){3}\d{1,3})'
# print(re.findall(pattern, content))
#
import re

s = '<html><h1>hello</h1></html>'
pattern = r'<(\w+)><(\w+)>.*</\2></\1>'
# print(re.findall(pattern, s))
matchObj = re.match(pattern, s)
if matchObj:
    # group方法返回满足条件的所有内容;
    print(matchObj.group())
    # groups方法返回满足条件的分组内容;
    print(matchObj.groups())
    print(matchObj.groupdict())





#

# url = "http://www.westos.org/jishu/book"
# pattern = r'http://(?P<domainName>.+)/(?P<type>\w+)/.+'
# matchObj =  re.match(pattern, url)
# if matchObj:
#     print(matchObj.group())
#     print(matchObj.groups())
#     res = matchObj.groupdict()
#     print(res['domainName'])