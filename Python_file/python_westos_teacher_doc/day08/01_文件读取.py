#!/usr/bin/env python
#coding:utf-8


""""
Name: 01_文件读取.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
# # open打开文件默认mode='r'
# f = open("/tmp/passwd")
# print(f)
# print(f.read())
# print("before-文件打开状态:",f.closed)
# f.close()
# print("after-文件打开状态:",f.closed)




# r,w,r+,w+,a,a+
# rb,wb,rb+,

# w:
#   1. 文件不存在， 则创建文件;
#   2. 'w'模式打开文件， 先清空文件的所有内容
#   3. read?(no)   write?(yes)

# f = open("/tmp/passwd1", 'w')
# # f.read()
# # f.write("hello")
# f.close()

# r
#   1. 文件不存在， 则报错;
#   2. 'r'模式打开文件， 不会清空文件的所有内容
#   3. read?(yes)   write?(no)
# f = open("/tmp/passwd", 'r')
# # f.write("hello")
# print(f.read())
# f.close()




# r+
#   1.
#   2.
#   3.






# a+
# 1. file not exist, create;
# 2. write(yes), read(yes)
# 3. 追加写入的内容到最后;

f = open("/tmp/passwd", 'a+')
f.write("\npython\n")
print(f.read())
f.close()





