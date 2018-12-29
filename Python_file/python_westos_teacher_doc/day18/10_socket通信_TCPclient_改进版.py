#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_socket通信_TCPserver_改进版.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

import socket

HOST = '172.25.254.250'
PORT = 9881
# 1.
with socket.socket() as clientSocket:
    # 2. 连接远程主机
    clientSocket.connect((HOST, PORT))

    # 3. 客户端， 服务端通信
    # 给server主机发送消息
    while True:
        cmd = input('client>>').encode('utf-8')
        clientSocket.send(cmd)
        # 接收服务端的响应(即服务端回复的消息)
        recvData = clientSocket.recv(1024).decode('utf-8')
        print("命令执行结果:", recvData)

# paramiko
