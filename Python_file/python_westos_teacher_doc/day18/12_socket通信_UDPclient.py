#!/usr/bin/env python
# coding:utf-8


""""
Name: 12_socket通信_UDPclient.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('172.25.254.250', 9999)

while True:
    msg = input('client>>')
    msg = msg.encode()
    client.sendto(msg, address)
    print("接收到服务端的消息:", client.recv(1024))
