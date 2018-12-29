#!/usr/bin/env python
#coding:utf-8


""""
Name: 05_while循环练习_猜数字游戏.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:

# 猜数字游戏


# if , while, break
# 1. 系统随机生成一个1～100的数字；
# 2. 用户总共有5次猜数字的机会；
# 3. 如果用户猜测的数字大于系统给出的数字，打印“too big”；
# 4. 如果用户猜测的数字小于系统给出的数字，打印"too small";
# 5. 如果用户猜测的数字等于系统给出的数字，打印"恭喜中奖100万",
并且退出循环；

"""
# 注意while循环可以和else结合；

import random

sys_num = random.randint(1,100)
guess_count = 0


while guess_count < 3:
    # 转换接收的字符串类型为整形
    guess_num = int(input("Guess Num:"))
    # 猜测次数加1
    guess_count += 1

    # 判断
    if guess_num > sys_num:
        print('tooy big')
    elif guess_num < sys_num:
        print('too small')
    else:
        # break跳出循环;
        print("恭喜中奖100万")
        break
else:
    print("尝试次数超过3次")



