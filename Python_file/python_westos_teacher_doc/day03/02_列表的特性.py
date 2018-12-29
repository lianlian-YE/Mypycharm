#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_列表的特性.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:

# 字符串的特性: 索引, 切片， 连接， 重复， 成员操作符;
"""
students_name = ['harry', 'westos', 'fentiao', 'natasha']



# 1. 索引
# 正向索引
print(students_name[0])
# 反向索引
print(students_name[-1])



# 2. 切片
print(students_name[::-1])

#
s = "hello xiao mi"   # "mi xiao hello"
print(" ".join(s.split()[::-1]))



# 3. 重复
print(students_name*3)


# 4. 连接
print(students_name + ['Bob', 'Lilei'])



# 5. 成员操作符
print('Bob' in students_name)
print('fentiao' in students_name)


# 6. for循环遍历列表元素
for student in students_name:
    print("学生姓名:%s" %(student))





# 7. 列表里面嵌套列表

goods = [
    ['apple', 2, 100],
    ['banana', 3, 50],
    ['computer', 4000, 13]
]
# 嵌套索引
print(goods[0][0])

