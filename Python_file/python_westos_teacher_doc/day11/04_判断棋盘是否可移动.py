#!/usr/bin/env python
# coding:utf-8


""""
Name: 04_判断棋盘是否可移动.py
Date: 2018/05/26
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

field = [
    [0, 0, 0, 0],
    [2, 2, 0, 0],
    [2, 0, 2, 0],
    [2, 4, 2, 2]
]


def move_left_possible(row):
    """判断列表中的一行是否可以移动"""
    # 0 2, 0 4, 2 2, 4 2
    # 0 0
    # # 1. 判断两个元素是否可以移动?
    # 4,2,2,2
    def is_change(i):
        if row[i] == 0 and row[i + 1] != 0:
            return True
        if row[i] != 0 and row[i + 1] == row[i]:
            return True
        return False

    # len(row)-1 =4-1 = 3
    # i= 0,1,2
    # 依次遍历每一行的每一个元素， 判断是否可以移动， 只要有一个时可以移动的， 返回True
    return any([is_change(i) for i in range(len(row) - 1)])


def invert(field):
    # 对于列表每一行进行反转
    return [row[::-1] for row in field]
def tranpose(field):
    """对于列表转置， 可以间接求向上移动的可能性"""
    return [list(row) for row in zip(*field)]




check = {}

check['Left'] = lambda  field:  any([move_left_possible(row) for row in field])
# check['Right'] = lambda  field: any([ move_left_possible(row) for row in invert(field)])
# 判断每行内容反转后的field能否向左移动， 即原field能否向右移动;
check['Right'] = lambda field: check['Left'](invert(field))
# 判断转置后的field能否向左移动， 即原field能否向上移动;
check['Up'] = lambda  field: check['Left'](tranpose(field))
# 判断转置后的field能否向右移动， 即原field能否向下移动;
check['Down'] = lambda  field: check['Right'](tranpose(field))

print(check['Left']([[2, 4, 2, 4], [2, 4, 2, 0], [2, 4, 2, 4], [2, 4, 2, 4]]))
print(check['Right']([[2, 4, 2, 4], [2, 4, 2, 0], [2, 4, 2, 4], [2, 4, 2, 4]]))
print(check['Up']([[2, 4, 2, 4], [2, 4, 2, 0], [2, 4, 2, 4], [2, 4, 2, 4]]))
print(check['Down']([[2, 4, 2, 4], [2, 4, 2, 0], [2, 4, 2, 4], [2, 4, 2, 4]]))



#
# check = {}
#
# check['Left'] = lambda field: any(move_left_possible(row) for row in field)
# check['Right'] = lambda field: check['Left'](invert(field))
# check['Up'] = lambda field: check['Left'](tranpose(field))
# check['Down'] = lambda field: check['Right'](tranpose(field))
#
# print(check['Left']([[2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4]]))
# print(check['Right']([[2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4]]))
# print(check['Up']([[2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4]]))
# print(check['Down']([[2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4]]))




# print(move_left_possible([2,4,0,0]))
# print(move_left_possible([0,0,2,4]))
