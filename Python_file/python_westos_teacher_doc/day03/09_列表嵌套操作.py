#!/usr/bin/env python
# coding:utf-8


""""
Name: 09_列表嵌套操作.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

import pprint

li1 = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]
li2 = [
    [2, 3, 4],
    [1, 2, 3],
    [1, 2, 3]
]

# numpy,  pandas, matplotlib
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

#  i : 0, 1, 2
for i in range(len(li1)):
    # j: 0, 1, 2
    for j in range(len(li1[i])):
        # [0][0], [0][1], [0][2]
        # [1][0]
        result[i][j] = li1[i][j] + li2[i][j]
pprint.pprint(result)
