#!/usr/bin/env python
# coding:utf-8


""""
Name: 05_协程理解.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


协程是一种允许在特定位置暂停或恢复的子程序——这一点和生成器相似。
但和生成器不同的是，协程可以控制子程序暂停之后代码的走向，而生
成器仅能被动地将控制权交还给调用者。



练习1:
假设有两个子程序main和printer。printer是一个死循环，等待输入、
加工并输出结果。main作为主程序，不时地向printer发送数据。


加工: [1] text
     [2] text
这应该怎么实现呢？
"""



def printer():
    counter = 1
    while True:
        text = yield
        print('[%d] %s' %(counter, text))
        counter += 1

def main():
    p = printer()
    next(p)
    # p.__next__()
    for i in range(10):
        p.send('Hi')
        p.send('hello python')
        p.send('hello gcc')
main()






