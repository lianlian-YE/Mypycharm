#!/usr/bin/env python
#coding:utf-8


""""
Name: 05_分布式进程.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


# 1. 进程间
# 2. 线程---不能用来作为不同主机间交流
# 3. 协程----不能用来作为不同主机间交流


# 目标: 实现分布式任务------多进程


# 如何实现?
multiprocessing不仅仅支持多进程, 而且其中的子模块managers支持将多进程分布到多台及其上;








"""


import multiprocessing
from multiprocessing import managers


# fork
# multiprocessing
# 进程间交流通过队列来实现;
