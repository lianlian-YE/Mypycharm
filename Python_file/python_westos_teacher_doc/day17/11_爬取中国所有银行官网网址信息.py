#!/usr/bin/env python
# coding:utf-8


""""
Name: 11_爬取中国所有银行官网网址信息.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
from urllib import request
from urllib.request import urlopen

import re

url = 'http://www.cbrc.gov.cn/chinese/jrjg/index.html'

#
# def get_content(url):
#     # 1. 模拟浏览器访问;
#     headers = {'User-agent': 'FireFox/12.0'}
#     req = request.Request(url, headers=headers)
#
#     with urlopen(req) as urlObj:
#         content =  urlObj.read().decode('utf-8')
#
#     with open('bank.txt', 'w') as f:
#         f.write(content)
#         print('write success')




def get_file_content(filName):
    with open('bank.txt') as f:
        return f.read().replace('\t', '')


def pattern_html():
    content = get_file_content('bank.txt')

    # < a href = "https://www.sc.com/cn/" target = "_blank" style = "color:#08619D">渣打银行</a>

    pattern1 = r'<a href="(https?://.+|www.+)" target="_blank"  style="color:#08619D">\s*(.+)'
    bank_li1 = re.findall(pattern1, content)
    return bank_li1


def write_to_file(filename, bank_li):
    with open(filename, 'w') as f:
        f.write("银行名称\tURL\n")
        for url,name in bank_li:
            f.write("%s\t%s\n" %(name.strip(), url))

    print("写入成功!")



bank_li = pattern_html()
for ur, name in bank_li:
    print(ur, '\t', name)
write_to_file('bank1.txt', bank_li)