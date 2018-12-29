#!/usr/bin/env python
# coding:utf-8


""""
Name: 03_协程爬取网页.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import gevent
from mytime import timeit
from gevent import monkey
import threading
# 打补丁， 自动修改协程中需要的一些标准库;
monkey.patch_socket()

def load_url(url):
    # print('get %s' % (url))
    with urlopen(url) as urlObj:
        content = urlObj.read().decode('utf-8')

    # print("%s网页有%s字节" % (url, len(content)))


URLS = ['http://httpbin.org', 'http://example.com/'] * 10

@timeit
def geventMain():
    jobs = [gevent.spawn(load_url, url) for url in URLS]
    gevent.joinall(jobs)


@timeit
def threadMain():
    with ThreadPoolExecutor(max_workers=100) as pool:
        pool.map(load_url, URLS)



geventMain()
threadMain()