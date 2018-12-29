#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_异常处理.py
Date: 2018/05/24
Connect: xc_guofan@163.com
Author: lvah
Desc:

try.....except..... finally
"""



# try:   #
#     a = 3
#     c = [1,2,3,4]
#     print(c[5])
#     print(b)
# except (NameError, IndexError)  as e:
#     pass
#
# # except   NameError as e:
# #     print(e)
# # except IndexError as e:
# #     print(e)
# print("hello")




try:
    f = open('/etc/passwd', 'r')
    print(a)
    f.close()
except NameError as e:
    pass
finally:
    f.close()

print(f.closed)


class AgeError(BaseException):
    pass


# 抛出异常
age  = int(input("Age:"))
if 0<age<100:
    print(age)
else:
    raise AgeError("年龄不合法")





