#!/usr/bin/env python
# coding:utf-8


""""
Name: 05_带有参数装饰器练习_参数检测.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:



# 1. 基础版(无参数的装饰器)
编写装饰器required_ints, 条件如下:
    1). 确保函数接收到的每一个参数都是整数;
    2). 如果参数不是整形数， 打印 TypeError:参数必须为整形

# 2. 升级版(有参数的装饰器)
编写装饰器required_types, 条件如下:
    1). 当装饰器为@required_types(int,float)确保函数接收到的每一个参数都是int或者float类型;
    2). 当装饰器为@required_types(list)确保函数接收到的每一个参数都是list类型;
    3). 当装饰器为@required_types(str,int)确保函数接收到的每一个参数都是str或者int类型;
    4). 如果参数不满足条件， 打印 TypeError:参数必须为xxxx类型

"""

def required_types(*types):
    def required(f):
        def wrapper(*args, **kwargs):  # args=(1,2)
            # 1. 判断每一个元素都是整形;
            for i in args:
                if not isinstance(i, types):
                    print("Error:参数必须为",types)
                    break
            else:
                res = f(*args, **kwargs)
                return res
        return wrapper
    return required
@required_types(int,float)
def add(x, y):
    return x + y
print(add(1, 2e+9))
