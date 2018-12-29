#!/usr/bin/env python
#coding:utf-8


""""
Name: 06_案例_web监控与邮件报警.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

from urllib.request import  urlopen

def url_OK(url):
    try:
        urlObj = urlopen(url)
        print(urlObj.code)
    except Exception as e:
        return False

url_OK('http://www.baidu.com/hell1o.html')