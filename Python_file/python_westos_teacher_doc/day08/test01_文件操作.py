#!/usr/bin/env python
#coding:utf-8


""""
Name: test01_文件操作.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:




这个文本文件核心有几种情况：
序号 ID 操作者 操作行为 操作行为 操作对象
6883 556773833 RemyMCMXI
6880 556772838 Mindmatrix restored undeleted RemyMCMXI
6882 556771715 RemyMCMXI
6881 556770863 RemyMCMXI
6880 556673938 Liua97
6879 554350969 Epicgenius
6880 554332653 Alex

找到restored所在行，得到该行序号6880，然后往下读，
找到第一个与其序号相同的行（liua97那行），
然后记录下这两行之间所有的id值（包括restored那行），
这个例子就是记录下556772838 556771715 556770863这三个id。


"""



