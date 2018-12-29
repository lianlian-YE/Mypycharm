#!/usr/bin/env python
# coding:utf-8


""""
Name: 04_集合练习.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:

1. 共同好友；
        你的好友A,B,C 他的好友C,B,D， 求共同好友：

2.   微信群提醒：
        XXX与群里其他人都不是微信朋友关系

s1, s2, s3

s1 = {s4, s5, s6}
s2 = {s1, s3, s6}


      s3 in (s1 | s2)




3. 权限判断：
        有一个API，要求同时具备A,B,C权限才能访问，目前用户权限为B,C,D，判断该用
户能否访问该API;



实质看用户权限是否为ABC的父集；


ABC     ABCD
ABC     ADF




4. 集合练习:
               随机产生2组各个数字的列表，每组10个数字，如下要求：
                    每个数字取值范围[10,20]
                    统计20个数字中，一共有多少个不同的数字？  # {1,2,3} {2,3,4} # 并集
                    2组中，不重复的数字有几个？分别是什么？{1,2,3} {1,2,4}  # 对等差分;
                    2组中，重复的数字有几个？分别是什么？




5. 一个总任务列表，储存所有任务，一个完成的任务列表。找出未完成的任务; # 实质上是求差集的。
all_task = ['task1', 'task2', 'task3']
complete = ['task1']





"""
import random


li1 = []
li2  = []
for i in range(10):
    li1.append(random.randint(10,20))
    li2.append(random.randint(10,20))


print(li1, li2)


s1 = set(li1)
s2 = set(li2)

print("20个数字中共有%s个不同的数字" %(len(s1 | s2)))

sy_set = s1.symmetric_difference(s2)

print(" 2组中，不重复的数字有%s个， 分别是%s" %(len(sy_set), sy_set))



inster_set = s1 & s2
print("2组中，重复的数字有%s个,分别是%s" %(len(inster_set), inster_set))



