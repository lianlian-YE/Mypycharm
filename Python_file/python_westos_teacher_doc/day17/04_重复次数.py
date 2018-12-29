#!/usr/bin/env python
#coding:utf-8


""""
Name: 04_重复次数.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:


*: 代表前一个字符出现0次或者无限次,  {0,}
+: 代表前一个字符出现一次或者无限次; 1, 100, 1000,   {1,}
?: 代表前一个字符出现1次或者0次; 可省略的字符;   {0,1}





******************更加精确表示出现的次数******************
\d{3} : 这个数字出现3次;


{m}: 代表前一个字符出现m次;
{m,}: 代表前一个字符出现m次或者>m次   >=m;
{m,n}: 代表前一个字符出现m次到n次之间   m~n;






188-?5643-7698
"""

import re
print(re.findall(r'1+', '读阅人数为1000, 11, 111, 100'))
print(re.findall(r'\d+', '读阅人数为1000, 11, 111, 100'))
print(re.findall(r'westo*s', 'westooos   wests westas'))






