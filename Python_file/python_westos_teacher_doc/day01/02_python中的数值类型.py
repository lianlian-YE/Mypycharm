#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_python中的数值类型.py
Date: 2018/04/21
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# 1. python中支持的数值类型: int,long,float, complex
aInt = 13
# 查看变量的数据类型
print(type(aInt))

aLong = 348237857984594350983294830481230483210
print(type(aLong))

# 在python3中不存在1L
# # 强制设置数值为长整形， 后加L/l;
# bLong = 1L
# cLong = 1l
# print(type(bLong))



aFloat = 1.3434
print(type(aFloat))


# '1223+33e2'
bFloat = 33e+2
cFloat = 33e-2
dFloat = 33e2
# eFloat = 33e   # 不是浮点数， ae+b(a,b为常量， 代表a*10^b)
print bFloat
print cFloat
print dFloat


## 复数类型: x**2>0, x**2=-1    # a+bi
aComplex = 2+3j
print type(aComplex)
print aComplex.real
print aComplex.imag
print aComplex.conjugate()



# 2. 数据类型的转换: 在python中， 所有的数据类型，都可以作为内置函数， 转换数据类型;
aInt = 2
transFloat = float(aInt)
print transFloat



print int(2.0)
print type(long(2.0))
print complex(2)


# 3. 如何删除内存中的变量;
print aInt
print "deleting aInt......."
del aInt
print aInt










