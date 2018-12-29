#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_应用案例_贴吧上爬取邮箱.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

from urllib import request

import re

url = 'http://tieba.baidu.com/p/2314539885'




def get_content(url):
    with request.urlopen(url) as f:
        content = f.read().decode('utf-8')
        return content


def get_page(url):
        content = get_content(url)
        # < a href = "/p/2314539885?pn=31" >尾页 < / a >
        pattern = r'<a href="/p/.*?pn=(.*)">尾页</a>'
        return int(re.findall(pattern, content)[0])

def create_url(url, page):

    url_li = []
    for i in range(page):
        print("第%s页" %(i+1))
        new_url = url+'?pn=%d' %(i+1)
        url_li.append(new_url)
    return url_li



def get_email(url):
    content = get_content(url)
    pattern = r"[a-zA-Z0-9_]+@\w+\.com"
    return re.findall(pattern, content)



page = get_page(url)
print("贴吧总共有%d页, 正在爬取中.......")


url_li = create_url(url,page)

for url in url_li:
    print(get_email(url))









