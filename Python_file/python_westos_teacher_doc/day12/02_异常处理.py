#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_异常处理.py
Date: 2018/05/27
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import os

high_score = 2048

def save_high_score():
    try:
        # 可能出现问题
        os.mknod('highscore.ini')
    except Exception as e:
        # 捕获异常
        print(e)
    with open('highscore.ini', 'w') as f:
        f.write(str(high_score))
        print("write score success!")
    return True


save_high_score()
high_score = 4096
save_high_score()
print('hello')










