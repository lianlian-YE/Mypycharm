#!/usr/bin/env python
#coding:utf-8


""""
Name: 02_参数传递optparses.py
Date: 2018/06/03
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


from optparse import OptionParser
import argparse




USAGE = "command [OPTION....]"
parser = OptionParser(USAGE)


# 新加属性：
# -s:  type:类型, dest: 传递的值赋值的变量名, help:帮助, default: 默认值
parser.add_option('-s',  type=int, dest='srcid', help="原账户id", default=610001)
parser.add_option('-d',  type=int, dest='destid', help='目标账户id', default=610002)
parser.add_option('-m',  type=float,dest='money', help='转账金额', default=500)


# 解析接收的属性值
option, args = parser.parse_args()

print(option)
print(args)
print(option.srcid)
print(option.destid)










