#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_socket通信_服务端.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:

ssh:
"""
import socket

HOST = '172.25.254.250'
PORT = 9888

# 1. 创建服务端的socket对象
serverSocket = socket.socket()
# 2. 绑定一个ip和端口， 客户端连接时的socket；
serverSocket.bind((HOST, PORT))
# 3. 一直监听是否有客户端连接
serverSocket.listen()
print("server is listening %d......." %(PORT))
# 4. 如果有客户端连接, 接收客户端的连接;
# serverSocket.accept会返回2个值, address指的是， 客户端的ip和端口;
clientSocket, address = serverSocket.accept()

# 5. 客户端和服务端进行通信;

data = clientSocket.recv(1024).decode('utf-8')
print("接收到客户端的消息:", data)


# 6. 给客户端回复消息
clientSocket.send(b'hello client')

# 7. 关闭socket对象, 一次通信完成;
serverSocket.close()
clientSocket.close()










