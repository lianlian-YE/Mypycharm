
#!/usr/bin/env python
#coding:utf-8


""""
Name: 16_字符串的搜索与替换.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


find(), replace()

"""

s = "hello world hello"

# find找到子串，并返回最小的索引值;
print(s.find("hello"))
print(s.find("world"))

# find找到子串，并返回最大的索引值;
print(s.rfind("hello"))


# 替换字符串中所有的“hello”为"westos"
print(s.replace("hello", "westos"))
