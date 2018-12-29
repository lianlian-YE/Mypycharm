#!/usr/bin/env python
# coding:utf-8


""""
Name: 06_抛出异常.py
Date: 2018/05/27
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# # 如何自定义异常类? 只需要从Exception类里面继承即可
# class AgeError(Exception):
#     pass
#
#
# try:
#     age = int(input('Age:'))
#     if not 0<age<150:
#         raise AgeError("age不合法")
#     else:
#         print("%s岁" %(age))
# except ValueError as e:
#     print(e)





# import sys
#
# try:
#     f = open('/tmp/passwd')
#     s = f.readline()
#     i = int(s.strip())
#     print(a)
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# # except NameError as e:
# #     print(e)
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
# else:
#     print('all success')
#
# print('hello')





# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:   # B， C， D
#     try:
#         # raise B
#         # raise C
#         # raise D
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")
