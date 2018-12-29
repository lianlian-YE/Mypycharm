#!/usr/bin/env python
# coding:utf-8


""""
Name: 22_字典生成式.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

#
# d = dict(a=1,b=2)
# print("小写的字典:", d)
#

# 1. 需求1： 将所有的key值变为大写;


## 1-1. 传统方法:
# new_d = {}
# for i in d:   # 'a' 'b'
#     new_d[i.upper()] = d[i]
# print("key转化为大写的字典:", new_d)

## 1-2. 升级
# print({k.upper():v for k,v in d.items()})



# # 需求2：大小写key值合并, 统一以小写key值输出;
d = dict(a=2, b=1, c=2, B=9, A=5)
## 2-2. 字典生成式:
print({k.lower():d.get(k.lower(),0)+d.get(k.upper(),0) for k in d})

# 2-1. 传统方法:
# # {'a':2, 'b':1, 'c':2}
# new_d = {}
#
# for k, v in d.items():
#     low_k = k.lower()
#     if low_k not in new_d:
#         new_d[low_k] = v
#     else:
#         new_d[low_k] += v
#
# print(new_d)







#
# new_d = {}
# for k,v in d.items():
#     lower_k = k.lower()
#     if lower_k in new_d:
#         new_d[lower_k] += d[k]
#     else:
#         new_d[lower_k] = d[k]
#
# print(new_d)



# new_d = {k.lower():d.get(k.lower(),0)+d.get(k.upper(),0) for k in d}
# print(new_d)



# # # 需求3： 把字典的key和value值调换；
# d = {'a':'1', 'b':'2'}
#
#
# print({v:k for k,v in d.items()})
