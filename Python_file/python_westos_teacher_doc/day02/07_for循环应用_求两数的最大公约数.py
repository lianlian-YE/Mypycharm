#!/usr/bin/env python
# coding:utf-8


""""
Name: 07_for循环应用_求两数的最大公约数.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


最大公约数:  两个数的约数中最大的那个;

"""

# 1. 输入两个数值: input接收字符串;
num1 = int(input('Num1:'))
num2 = int(input('Num2:'))

# 2. 找出两数中最小的值;
min_num = min(num1, num2)

# 3. 最大公约数在1~min_num之间存在， 如果num1和num2能整除的最大的数为最大公约数;
for i in range(1, min_num + 1):
    if num1 % i == 0 and num2 % i == 0:  # i=1, i=2
        # 当循环完，res中保存的是最大的约数；
        res = i

# 最小公倍数=(num1*num2)/最大公约数;
lcm = int((num1 * num2) / res)

print("%s和%s的最大公约数为:%s" % (num1, num2, res))
print("%s和%s的最小公倍数为:%s" % (num1, num2, lcm))
