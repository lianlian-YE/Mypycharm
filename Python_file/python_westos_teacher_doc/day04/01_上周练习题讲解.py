#!/usr/bin/env python
#coding:utf-8


""""
Name: 01_上周练习题讲解.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""





# 3. # (2017-小米-句子反转)
# s = input("str:")
# if len(s) < 1000:
#     print(" ".join(s.split()[::-1]))
# else:
#     print('invaild string!')







#



s1 = input("s1:")
s2 = input("s2:")
for i in s2:
    if i in s1:
        s1 = s1.replace(i, "")
print(s1)








#

s = input("s:")



if s.isupper():
    s_len = len(s)
    # "HELO"   # H E, EL, LO,  (0, 1, 2)
    # range(4)   # [0, 1,2,3]

    for index in range(s_len-1):
        if s[index] == s[index+1]:
            print('Dislike')
            break
    else:
        print('Likes')
else:
    print('Dislike')
