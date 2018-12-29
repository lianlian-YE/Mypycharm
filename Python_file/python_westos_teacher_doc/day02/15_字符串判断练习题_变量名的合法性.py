#!/usr/bin/env python
#coding:utf-8


""""
Name: 15_字符串判断练习题_变量名的合法性.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:



# 变量名是否合法?
#
# 变量名可以由字母，数字或者下划线;
# 变量名只能以字母或者下划线开头;

s = "hello@"

1. 判断变量名的第一个元素是否为字母或者下划线; s[0]
2. 如果第一个元素符合条件， 判断除了第一个元素的其他元素;s[1:]

"""


# 1. for循环:依次遍历字符串的每一个元素;
# for i in "hello":  # i: 'h', 'e', 'l'    s[
#     if i.isalpha():
#         print(i)



#
# var = "hello'

# var = input("变量名:")
# # 判断第一个字符是否合法;
# if var[0] == "_" or var[0].isalpha():
#     for char in var[1:]:  # 判断除了第一个字符之外的其他字符 # char: e,l,l,o
#         if char.isalnum() or char == "_":
#             continue
#         else:
#             print('变量名%s不合法' %(var))
#             break
#     else:
#         print('变量名%s合法' %(var))
# else:
#     print("变量名不合法:第一个字符错误!")








var = input("变量名:").strip()
# 判断第一个字符是否合法;
if var[0] == "_" or var[0].isalpha():
    for char in var[1:]:  # 判断除了第一个字符之外的其他字符 # char: e,l,l,o
        if not (char.isalnum() or  char == "_"):
            print('变量名%s不合法' %(var))
            break
    else:
        print('变量名%s合法' %(var))
else:
    print("变量名不合法:第一个字符错误!")


