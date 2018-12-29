#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_常见的异常.py
Date: 2018/05/27
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# NameError
# print(a)


# IndexError
# li = [1,2,3]
# print(li[4])


# KeyError
# d = dict(a=1, b=2)
# print(d['c'])


# ZeroDivisionError
# print(10/0)



# ModuleNotFoundError
# import hello



# 捕获指定的异常: try.....except,  try.....except...else.....

# try:
#     l = [1,2,3]
#     print(l[2])
#     print(l)  # NameError
#     # 10/0
#     print("hello")
# except NameError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except Exception as e:
#     print('unknown error')
# else:
#     # 当try里面的代码全部成功， 没有任何异常错误， 则执行;
#     print('all operator ok')
# print("ok")






try:
    l = [1,2,3]
    print(l[2])
    print(l)  # NameError
    # 10/0
    print("hello")
# except语句可以以元组的方式同时指定多个异常;
except (NameError,IndexError) as e:
    print(e)
except Exception as e:
    print('unknown error')
else:
    # 当try里面的代码全部成功， 没有任何异常错误， 则执行;
    print('all operator ok')
print("ok")
