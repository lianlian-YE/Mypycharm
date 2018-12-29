#!/usr/bin/env python
#coding:utf-8


""""
Name: 01_python输入与输出.py
Date: 2018/04/21
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 1. python的输出:
# python2： print "要打印的字符串"
# python3： print("要打印的字符串")


name = "python"
print("hello %s" %(name))

sid = 1
print("hello %.3d" %(sid))



# 2. python的输入：
# python2:
# raw_input(): 接收字符串的数据;
# input(): 只能接收数值；类型;

# python2的操作
# name = raw_input("input name:")
# print name
#
# info = input("input:")
# print info

# python3操作: 没有raw_input，只有input，
# python3中为了避免记忆困难， 用input接收数据， 为字符串类型;
name = input("Name:")
print(name)


age = input("Age:")
print(age,type(age))





"""
print "%s" %(001)
1
print "%d" %(001)
1
print "%d" %(0011)
9
print "%o" %(9)
11
print "%o" %(10)
12
print "%o" %(11)
13
print "%x" %(16)
10
print "%x" %(17)
11
print "%x" %(11)
b
print "%f" %(11)
11.000000
print "%.3f" %(11)
11.000
print "%.2f" %(11)
11.00
print "内存占有率:%.2f%" %(1.23324546456)
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/IPython/core/interactiveshell.py", line 2882, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-21-5446e13955af>", line 1, in <module>
    print "内存占有率:%.2f%" %(1.23324546456)
ValueError: incomplete format
print "内存占有率:%.2f%%" %(1.23324546456)
内存占有率:1.23%
print "内存占有率:%10.2f%%" %(1.23324546456)
内存占有率:      1.23%
print "内存占有率:%-10.2f%%" %(1.23324546456)
内存占有率:1.23      %
"""











