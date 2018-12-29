#!/usr/bin/env python
# coding:utf-8


""""
Name: 05_案例_自动带伞提醒程序.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import json
from urllib.request import urlopen
from urllib import request

# 1. 如何获取网页上的内容?
# 目标: 获取baidu主页的内容;
# url = 'https://www.baidu.com/'
#
# urlObj = urlopen(url)
# urlContent = urlObj.read()
# print(urlContent)





# 2. 获取中国天气网， 西安的天气；(有问题, 如果是python脚本获取网页内容， 则禁止； 如果是浏览器， 则不禁止;)
# url = "http://www.weather.com.cn/data/cityinfo/101110101.html"
#
# urlObj = urlopen(url)
# urlContent = urlObj.read()
# print(urlContent)
#

# 3. 伪装成浏览器访问url地址;
# url = "http://www.weather.com.cn/data/cityinfo/101110101.html"
# headers = {'User-Agent': 'Firefox/23.0'}
# req = request.Request(url, headers=headers)
# urlObj = urlopen(req)
# urlContent = urlObj.read().decode('utf-8')
# print(urlContent)





# 4. 将读取网站内容的步骤封装成函数;
def readUrl(url):
    # 生成字典， 指定用户代理为火狐浏览器， 而不是python脚本;
    headers = {'User-Agent': 'Firefox/23.0'}
    # 向url地址发起请求, 返回一个Request对象;
    req = request.Request(url, headers=headers)
    # 返回一个urlOpen对象， 该对象中包含访问的所有结果， 比如: 网页内容, 网页的状态码(200, 404)
    urlObj = urlopen(req)
    # 将读取的内容以utf-8编码显示;(中文显示不乱码)
    urlContent = urlObj.read().decode('utf-8')
    return  urlContent






#5. json格式

# d = {'name':'fentiao', 'age':10}
# # 把字典编码成json格式的字符串;
# json_d = json.dumps(d)
# print(json_d, type(json_d))
#
# # 将json格式的子符串解码为python可以识别的数据类型;
# d1 = json.loads(json_d)
# print(d1, type(d1))

# d = {'name': 'fentiao', 'age': 10}
# json_d = json.dumps(d)
# with open('test.json', 'w') as f:
#     f.write(json_d)

# with open('test.json') as f:
#     content = f.read()
#     d1 = json.loads(content)
#     print(d1, type(d1))

def sendMail():
    pass

def main():
    url = "http://www.weather.com.cn/data/cityinfo/101110101.html"
    info = readUrl(url)
    d = json.loads(info)
    weather = d['weatherinfo']['weather']

    if '雨' in weather or '雪' in weather:
        sendMail()

main()