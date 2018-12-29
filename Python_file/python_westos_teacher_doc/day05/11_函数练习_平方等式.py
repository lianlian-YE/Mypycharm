#!/usr/bin/env python
# coding:utf-8


""""
Name: 11_函数练习_平方等式.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


题目需求:
    对于一个十进制的正整数， 定义f(n)为其各位数字的平方和，如:
    f(13) = 1**2 + 3**2 = 10
    f(207) = 2**2 + 0**2 + 7**2 = 53

    下面给出三个正整数k，a, b,你需要计算有多少个正整数n满足a<=n<=b,
    且k*f(n)=n

输入:
    第一行包含3个正整数k，a, b, k>=1,  a,b<=10**18, a<=b;
输出：
    输出对应的答案;

范例:
    输入: 51 5000 10000
    输出: 3













"""


# k*f(n)=n

def f(n):
    res = 0
    for item in str(n):
        res += int(item) ** 2
    return res

def isOk(k, n):
    if k * f(n) == n:
        return True
    else:
        return False


def main():
    k = 51
    a = 5000
    b = 10000
    count = 0
    for i in range(a, b + 1):
        if isOk(k, i):
            count += 1

    print(count)

main()


