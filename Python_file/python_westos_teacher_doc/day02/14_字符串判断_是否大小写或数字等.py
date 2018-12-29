#!/usr/bin/env python
#coding:utf-8


""""
Name: 14_字符串判断_是否大小写或数字等.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


[[:digit:]]
[[:upper:]]
[[:lower:]]
[[:alnum:]]
[[:space:]]

"""



s = 'hello'


# 判断字符串里面的每个元素是否为什么类型， 一旦有一个元素不满足， 返回False;
print("123".isdigit())
print("123hfjhre".isdigit())
print("HELLO".isupper())
print("HELlO".isupper())

# title是标题， 判断某个字符串是否为标题, 第一个字母为大写，其他为小写;
print('Hello'.istitle())
print('HeLlo'.istitle())


print("hello".isnumeric())
print("111".isnumeric())







