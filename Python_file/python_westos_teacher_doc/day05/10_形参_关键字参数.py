#!/usr/bin/env python
#coding:utf-8


""""
Name: 10_形参_关键字参数.py
Date: 2018/05/05
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# **kwargs关键字参数; 接收的kwargs是字典类型;
def fun(**kwargs):
    print(kwargs, type(kwargs))


#
# fun(a=1, b=2)

#
# d = {
#      'a':1,
#      'b':2
#      }
#
# fun(**d)  # a=1,b=2



# <div id="s_tab"  width=100px  height=200px>网页</div>


def make_html(label, value, **kwargs):
    s = ""
    for k,v in kwargs.items():
        s += " %s=%s" %(k,v)

    html = "<%s %s>%s</%s>" %(label, s, value, label)
    return html
print(make_html("div", "网页",id="s_tab",width=100, height=200))






