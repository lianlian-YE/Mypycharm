#!/usr/bin/env python
#coding:utf-8


""""
Name: 05_棋盘移动.py
Date: 2018/05/26
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
# tight()   merge()  tight()
# [0,2,2,4]=== [2,2,4,0] == [4,0,4,0] == [4,4,0,0]



score = 0
def tight(row):
    """把所有非0的聚集在最左边"""
    # [0,2,2,4]  === [2,2,4]
    new_row = [item for item in row if item!=0]
    # if len(new_row) != len(row):
        # [2,2,4]+ [0] ==> new_row=new_row+[0]
    # range(0)不报错;
    new_row += [0 for item in range(len(row)-len(new_row))]
    return new_row

def merge(row):
    # 从左向右依次遍历， 如果两个值相等， 那么左边*2， 右边=0，
    for i in range(len(row)-1):  # 0,1,2,3
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
            global  score
            score += row[i]
    return  row


print(tight(merge([2,2,0,0])))
print(tight(merge([2,2,2,0])))
print(tight(merge([2,2,2,2])))


