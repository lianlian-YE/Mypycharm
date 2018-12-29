#!/usr/bin/env python
# coding:utf-8


""""
Name: 06_文件读取练习_京东二面编程题.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:
# 1. 生成一个大文件ips.txt,要求1200行， 每行随机为172.25.254.0/24段的ip;
# 2. 读取ips.txt文件统计这个文件中ip出现频率排前10的ip;
"""

import random
from collections import Counter


def create_ips_file(filename):
    ips = ['172.25.254.' + str(i)  for i in range(1, 255)]
    with open(filename, 'a+') as f:
        for count in range(120000):
            f.write(random.sample(ips,1)[0]+'\n')


# create_ips_file('ips.txt')



def sorted_by_ip(filename, count=10):
    ips_dict = dict()

    with open(filename) as f:
        for ip in f:
            if ip in ips_dict:
                ips_dict[ip] += 1
            else:
                ips_dict[ip] = 1
    sorted_ip = sorted(ips_dict.items(),key=lambda x:x[1],
                       reverse=True)[:count]
    return sorted_ip
    # return [ip[0].strip() for ip in sorted_ip]
print(sorted_by_ip('ips.txt'))

#
from collections import Counter
def new_method_sorted_by_ip(filename):
    with open(filename) as f:
        ipcount = Counter(f)
    print(ipcount.most_common(10))
new_method_sorted_by_ip("ips.txt")