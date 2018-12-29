#!/usr/bin/env python
#coding:utf-8


""""
Name: 11_字典练习1_重复的单词.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:




# 重复的单词: 此处认为单词之间以空格为分隔符， 并且不包含，和.；
    # 1. 用户输入一句英文句子；
    # 2. 打印出每个单词及其重复的次数;
"""


s = input("s:") # "hello java hello python"
# hello 3
# java 2
# python 1


# 1. 把每个单词分割处理;
s_li = s.split()
print(s_li)


# 2. 通过字典存储单词和该单词出现的次数;
words_dict = {}


# 3.
"""
# 依次循环遍历列表， 
    如果列表元素不在字典的key中，将元素作为key， 1作为value加入字典; 
    如果列表元素在字典的key中，直接更新value值， 即在原有基础上加1 
li = ['hello', 'java', 'hello', 'python']
words_dict = {'hello':2,'java':1 }
"""


for item in s_li:
    if item not in words_dict:
        words_dict[item] = 1
    else:
        # words_dict[item]  = words_dict[item] + 1
        words_dict[item]  +=  1

# 4. 打印生成的字典;
print(words_dict)













