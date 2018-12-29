#!/usr/bin/env python
#coding:utf-8


""""
Name: 11_socket通信_UDPserver.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import socket


# TCP: 9999
# UDP:9999
HOST = '172.25.254.250'
PORT = 9999
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 绑定端口:
server.bind((HOST, PORT))

# 不需要调用监听方法
print('等待客户端的UDP请求.....')

while True:
    # 接收客户端的数据
    data, addr = server.recvfrom(1024)
    print("接收到客户端的信息:", data)
    print("客户端的socket地址为:", addr)

    recv_data = input("server>>").encode()
    server.sendto(recv_data, addr)
