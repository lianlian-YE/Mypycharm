#!/usr/bin/env python
# coding:utf-8


""""
Name: 03_画2048游戏的棋盘.py
Date: 2018/05/26
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
from random import choice, randint

width = 4
height = 4

field = [[0 for i in range(width)] for j in range(height)]


def random_create():
    """初始化棋盘时， 在随机位置生成2或者4， 2的可能性大， 4的可能性少"""
    # 可能出现的问题: 随机生成的i,j位置原本已经有值。 解决方法：
    while True:
        i, j = choice(range(width)), choice(range(height))
        if field[i][j] == 0:
            field[i][j] = 4 if randint(1, 100) > 80 else 2
            break


random_create()
random_create()
print(field)

def draw_sep():
    line = '+' + '----+' * width
    print(line)
def draw_row(row):  # [2,0,2,0]
    draw_one_row = "".join(['|{:^4}'.format(num)
                        if num!=0  else '|    ' for num in row])+'|'

    print(draw_one_row)

def draw_field():
    for row in field:
        draw_sep()
        draw_row(row)
    draw_sep()

draw_field()


    # all_s = []
    # for num in row:
    #     if num != 0:
    #         a = '|{:^5}'.format(num)
    #         all_s.append(a)
    #     else:
    #         a = '|      '
    #         all_s.append(a)
    #
    # print("".join(all_s)+'|')

# draw_row([2,0,2,0])