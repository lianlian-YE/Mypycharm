#!/usr/bin/env python
# coding:utf-8


""""
Name: 14_函数练习.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:



1.Collatz序列
编写一个名为collatz()的函数,它有一个名为number的参数。
如果参数是偶数,那么collatz()就打印出number//2,并返回
该值。如果number是奇数,collatz()就打印并返回3*number+1。
然后编写一个程序,让用户输入一个整数,并不断对这个数
调用collatz(),直到函数返回值1(令人惊奇的是,这个序列
对于任何整数都有效,利用这个序列,你迟早会得到1!既使数学
家也不能确定为什么。你的程序在研究所谓的“Collatz序列”,
它有时候被称为“最简单的、不可能的数学问题”)。




- 输入:
    3

- 输出:
    10
    5
    16
    8
    4
    2
    1

"""


# def collatz(number):
#     # 为偶数
#     if number % 2 == 0:
#         return number // 2
#     else:
#         return 3 * number + 1
#
#
# def main():
#     num = int(input('Num:'))  # 3
#     while True:
#         if collatz(num) == 1:  # collatz(3) 3, 10, 2
#             print(1)
#             break
#         else:
#             num = collatz(num)
#             print(num)
#
#
# main()



def collatz(number):
    if number == 1:
        exit(0)
    elif number %2 == 0:
        return number // 2
    else:
        return 3 * number + 1


num = int(input('Num:'))
while True:
    num = collatz(num)
    print(num)