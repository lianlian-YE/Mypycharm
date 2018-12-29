#!/usr/bin/env python
#coding:utf-8


""""
Name: 12_字典练习2_数字重复统计.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


# 数字重复统计:
    1). 随机生成1000个整数;
    2). 数字的范围[20, 100],
    3). 升序输出所有不同的数字及其每个数字重复的次数;


"""
import random


# 1). 随机生成1000个整数;
all_nums = []
for item in range(1000):
    # 2).数字的范围[20, 100],
    all_nums.append(random.randint(20,100))


# # 3). 升序输出所有不同的数字及其每个数字重复的次数;
#
#
# # - 对生成的1000个数字进行排序， 然后在加入到字典中，计算个数;
# sorted_nums = sorted(all_nums)
# nums_dict = {}
# for num  in sorted_nums:
#     if num in nums_dict:
#         nums_dict[num] += 1
#     else:
#         nums_dict[num] = 1
# print(nums_dict)






nums_dict = {}
for num  in all_nums:
    if num in nums_dict:
        nums_dict[num] += 1
    else:
        nums_dict[num] = 1

sort_num_dict = {}
print(sorted(nums_dict.keys()))
#
for num in sorted(nums_dict.keys()):
    sort_num_dict[num]=  nums_dict[num]

print(sort_num_dict)



