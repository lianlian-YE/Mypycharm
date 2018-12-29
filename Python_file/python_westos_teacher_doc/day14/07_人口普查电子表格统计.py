#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_人口普查电子表格统计.py
Date: 2018/06/03
Connect: xc_guofan@163.com
Author: lvah
Desc:


有一张电子表格的数据,来自于 2010 年美国人口普查.

提示:
	censuspopdata.xlsx 电子表格中只有一张表,名为'Population by Census Tract'。每
一行都保存了一个普查区的数据。列分别是普查区的编号(A),州的简称(B),县的名称(C),普查区的人口(D)。


目标:
	编写一个脚本,从人口普查电子表格文件中读取数据,并在几秒钟内计算出每个县的统计值。


步骤:
	从 Excel 电子表格中读取数据。
	计算每个县中普查区的数目。
	计算每个县的总人口。
	打印结果。



dict = {
    '州':{
        '县1': {'pop':9000, '人口普查区'：2}，
    }，

}

dict[][]['pop']

"""



