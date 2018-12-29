#!/usr/bin/env python
# coding:utf-8


""""
Name: 02_集合操作.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# s = {1, 2, 3, 1, 2, 3}
# print(s)
#
# # 去重
# li = [1, 2, 3, 1, 2, 3]
# print(list(set(li)))

# s1 = {1, 2, 3}
# s2 = {1, 2, 4}

# print("并集:", s1.union(s2))
# print("交集：", s1.intersection(s2))
# # 求交集时， 把s1的值更新为交集的值;
# s1.intersection_update(s2)
# print(s1)



# print(s1.difference(s2))    # s1-instersection(s1,s2)
# print(s2.difference(s1))    # s2-intersection(s1,s2)
#
#
# # 求差集时， 把s2的值更新为差集的值;
# print(s2.difference_update(s1))    # s2-union(s1,s2)
# print(s2)


# s1 = {1, 2, 3}
# s2 = {1, 2, 4}
# # 对等差分;
# print(s1.symmetric_difference(s2))

#
# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s2 - s1)
#
# math = ['name1', 'name2']
# english = ['name1']




s1 = {1, 2, 3}
s2 = {1, 2, 4}


# s1是s2的子集？
print(s1.issubset(s2))
# s1是s2的父集？
print(s1.issuperset(s2))

# s1和s2没有交集么? 如果没有交集True，否则返回False;
print(s1.isdisjoint(s2))