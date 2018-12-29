#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_qrcode第三方模块应用.py
Date: 2018/05/12
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import qrcode




def main():
    img = qrcode.make("http://www.python.org")
    img.get_image().show()
    img.save('hello_python.png')






if __name__ == "__main__":
    main()