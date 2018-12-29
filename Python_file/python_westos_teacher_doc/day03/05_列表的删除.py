#!/usr/bin/env python
#coding:utf-8


""""
Name: 05_列表的删除.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


names = ['fentiao', 'fendai', 'fensi', 'apple', 'fendai']


# remove: 删除指定的值
names.remove('fendai')
print(names)

# names.pop(): pop删除指定索引的值， 默认情况删除最后一个元素;
# a = name.pop(), a就是删除的那个元素;
value = names.pop(0)
print(value)
print(names)



# del删除列表元素
# del names[0]
# del names[-1]
# del names[1:]
# del names[:-1]
# del names


# # clear: 清空列表
# names.clear()
# print(names)

