#!/usr/bin/env python
# coding:utf-8


""""
Name: 11_线程池.py.py
Date: 2018/06/07
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import threading
from collections import Iterable
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


# (python3.4以后的可以使用)
# *******************线程池的第一种方式***********************
import time
from queue import Queue


def hello(name, age):
    # time.sleep(2)
    print(name)

pool = ThreadPoolExecutor(max_workers=3)
print(pool.submit(hello,'hello', 1).result())
# pool.submit(hello, 'hello1')
# pool.submit(hello, 'hello2')
# pool.submit(hello, 'hello3')


from urllib.request import urlopen

import time

# 'https://api.github.com/'
URLS = ['http://httpbin.org', 'http://example.com/','http://httpbin.org', 'http://example.com/' ]


def load_url(url, timeout=3):
    """爬取指定的网页内容"""
    # urlObj = urlopen(url, timeout=timeout)
    # return urlObj.read()
    # with安全上下文管理:
    with urlopen(url, timeout=timeout) as urlObj:
        return urlObj.read()


def main1():
    with ThreadPoolExecutor(max_workers=4) as pool:
        # 将结果保存到字典中, key值是future对象, value值为url名称;
        # 字典生成式
        future_url = {pool.submit(load_url, url, 3): url for url in URLS}

        for future in as_completed(future_url):
            url = future_url[future]
            try:
                data = future.result()
            except Exception as e:
                print("%s 下载网页失败" % (url))
            else:
                print("%s 网页有 %s字节" % (url, len(data)))



def noThread():
    for url in URLS:
        try:
            data = load_url(url)
        except Exception as e:
            print("%s 下载网页失败" % (url))
        else:
            print("%s 网页有 %s字节" % (url, len(data)))




def mapThread():
    with ThreadPoolExecutor(max_workers=3) as pool:
        # map函数返回值为一个生成器， 每一个元素是load_url的返回值
        # zip('123', "abc"))  [(1,a), (2,b), (3,c)]
        datas = zip(URLS, pool.map(load_url,URLS))
        for url, content  in datas:
            print("%s 有%s字节" %(url, len(content)))






# map方法实现线程池任务的执行
# map(int, [1,2,3,4,5])


#
# start = time.time()
# main1()
# end = time.time()
# print("main1 run %.2f" % (end - start))
#
# start = time.time()
# noThread()
# end = time.time()
#
# print("noThread run %.2f" % (end - start))
#
#
# start = time.time()
# mapThread()
# end = time.time()
# print("mapThread run %.2f" % (end - start))
#



#
g = (i for i in range(5))
str = "hello"



z = zip(g, str)
print(isinstance(z, Iterable))
for i,j in z:
    print(i,j)