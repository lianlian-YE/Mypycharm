#!/usr/bin/env python
# coding:utf-8


""""
Name: 13_字符串开头和结尾匹配.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 找出字符串是否以xxxx结尾；
s = "hello.jpg"
print(s.endswith(('.png', '.jpg')))

url1 = "http://www.baidu.com"
url2 = "file:///mnt"
url3 = "https://www.baidu.com"
url4 = "ftp://www.baidu.com"

# 以什么开头;
print(url1.startswith(('https://', 'http://')))
print(url2.startswith("file://"))
