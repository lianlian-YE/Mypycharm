#!/usr/bin/env python
# coding:utf-8


""""
Name: 18_元组的理解.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 列表: 打了激素的数组;
# 元组: 带了紧箍咒的列表，
names = ['a', 'b', 'c', 1, 1.0, [1, 2]]
tuple_names = (1, 1.0, 2 + 4j, "hello", [1, 2], 10)


print(type(names), type(tuple_names))

# 验证元组的确是不可变的。
# tuple_names[0] = 1


print(tuple_names.index(1))
print(tuple_names.count(1))


# 元组的特性:
# 索引， 切片， 连接， 重复， 成员操作符， for循环
print(tuple_names[0])
print(tuple_names[-1])


print(tuple_names[1:])
print(tuple_names[:-1])
print(tuple_names[::-1])

print(tuple_names + (1,2,43))


# 不同数据类型可以连接么?(除了数值类型之外， 不同数据类型之间不可以连接)
# print([1,2,3]+ (1,2,4))
# print('hello'+[1,2,3])
print(1+2+4j)


print(tuple_names*3)



print(1 in tuple_names)
print(1 not in tuple_names)











