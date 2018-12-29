#!/usr/bin/env python
# coding:utf-8


""""
Name: 04_协程实现贴吧邮箱筛选.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib import request
import re
from gevent import monkey
import threading
# 打补丁， 自动修改协程中需要的一些标准库;
monkey.patch_socket()
import gevent

from mytime import timeit

url = 'http://tieba.baidu.com/p/2314539885'
EmailLi = []

def get_content(url):
    """获取网页源代码"""
    # 1. 下载网页源代码到本地, 获取帖子总页数;
    # urlObj = request.urlopen(url, timeout=60)
    # content = urlObj.read().decode('utf-8')
    with request.urlopen(url, timeout=60) as urlObj:
        content = urlObj.read().decode('utf-8')
        return content


def get_page(url):
    content = get_content(url)
    # <a href="/p/2314539885?pn=31">尾页</a>
    pattern = r'<a href="/p/.*pn=(\d+)">尾页</a>'
    page = re.findall(pattern, content)[0]
    return int(page)


def get_all_url(url, page):
    """生成所有页的帖子url地址"""
    url_li = []
    # page: 31  0,1,2,3,4.....30

    for i in range(page):
        new_url = url + '?pn=%d' %(i+1)
        url_li.append(new_url)
    return url_li


def get_email(url):
    content = get_content(url)
    pattern = r'[a-zA-Z0-9_]+@\w+\.com'
    EmailLi.extend(re.findall(pattern, content))
    print(re.findall(pattern, content))


@timeit
def useThreadMain():
    page = get_page(url)
    url_li = get_all_url(url, page)
    with ThreadPoolExecutor(max_workers=50) as pool:
        for urlItem in url_li:
            pool.submit(get_email, urlItem)

        # for future in as_completed(future_li):
        #     print(future.result())

@timeit
def useThreadMapMain():
    page = get_page(url)
    url_li = get_all_url(url, page)
    with ThreadPoolExecutor(max_workers=50) as pool:
        pool.map(get_email, url_li)

@timeit
def useNoThreadMain():
    page = get_page(url)
    url_li = get_all_url(url, page)
    for urlItem in url_li:
        print(get_email(urlItem))

# 结论:
#   1.  如果代码是IO密集型, 建议选择多线程;
#   2.  如果是计算密集型, 建议选用多进程；
# useNoThreadMain()
# useThreadMain()
# useThreadMapMain()
# print(EmailLi)
# print(len(EmailLi))


@timeit
def geventMain():
    url = 'http://tieba.baidu.com/p/2314539885'
    page = get_page(url)
    url_li = get_all_url(url, page)
    gevents = [gevent.spawn(get_email, url) for url in url_li]
    gevent.joinall(gevents)
geventMain()