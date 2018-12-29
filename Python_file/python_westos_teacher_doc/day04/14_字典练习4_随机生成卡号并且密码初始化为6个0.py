#!/usr/bin/env python
#coding:utf-8


""""
Name: 14_字典练习4_随机生成卡号并且密码初始化为6个0.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


# 1. 随机生成100个卡号；
#     卡号以6102009开头， 后面3位依次是 （001， 002， 003， 100），
# 2. 生成关于银行卡号的字典， 默认每个卡号的初始密码为"redhat";

# 3. 输出卡号和密码信息， 格式如下:
卡号                  密码
6102009001              000000

"""
# 存储所有卡号的列表， 也可以通过集合来存储;
card_ids = []

# 生成100个卡号的过程;
for i in range(100):
    # %.3d代表这个整形数占3位。 eg: 1--> 001;
    s = "6102009%.3d" %(i+1)
    # 将每次生成的卡号加入列表中;
    card_ids.append(s)

card_ids_dict = {}.fromkeys(card_ids, 'redhat')
# print(card_ids_dict)


print("卡号\t\t\t\t\t密码")
for key in card_ids_dict:
    print("%s\t\t\t%s" %(key, card_ids_dict[key]))


"""
# print({}.fromkeys('hello', 'redhat'))


"""