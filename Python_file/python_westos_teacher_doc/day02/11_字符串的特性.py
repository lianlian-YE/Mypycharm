#!/usr/bin/env python
#coding:utf-8


""""
Name: 11_字符串的特性.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
s = "hello"
# 索引： 0，1，2，3，4, 索引值是从0开始的;
print(s[0])
print(s[4])
print(s[-1])        # 拿出字符串的最后一个子符;

# 切片
print(s[0:3])       # 切片时规则为s[start:end:step],从start开始，到end-1结束， 步长为step;
print(s[0:4:2])


print(s[:])             # 显示所有子符

print(s[:3])            # 显示前3个子符
print(s[::-1])          # 对于字符串倒序输出;
print(s[1:])            # 除了第一个子符之外， 其他全部显示;

# 重复
print(s*10)

# 连接
print("hello "+"world")

# 成员操作符 s = "hello", in, not in
print('he' in s)
print('aa' in s)
print('he' not in s)










