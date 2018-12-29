#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_socket通信客户端.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:



# socket: {ip:port}
"""

import socket

HOST = '172.25.254.250'
PORT = 9888
# 1.
clientSocket = socket.socket()

# 2. 连接远程主机
clientSocket.connect((HOST, PORT))

# 3. 客户端， 服务端通信
# 给server主机发送消息
clientSocket.send(b'hello server')
# 接收服务端的响应(即服务端回复的消息)
recvData = clientSocket.recv(1024).decode('utf-8')
print("接收到服务器的消息:", recvData)
# 4. 关闭socket对象:
clientSocket.close()














# import socket
# # 1. 如何创建socket;
#
# # family:
# #       socket.AF_INET: 指定通过IPV4进行通信
# #       socket.AF_INET6: 指定通过IPV6进行通信
# # type:
# #       socket.SOCK_STREAM: 通过TCP通信
# #       socket.SOCK_DGRAM: 通过UDP通信
#
# s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# host = 'www.baidu.com'
# port = 80
#
#
# # 1. 连接百度, 获取本机与百度通信的ip和端口;
# s.connect((host, port))
# print("连接百度成功!")
# print(s.getsockname())
#
# # 2. 给百度发送消息;
# message = b'GET / HTTP/1.1\r\n\r\n'
#
# try:
#     # 发送请求网页内容的信息;
#     s.sendall(message)
# except socket.error:
#     print("发送请求失败!")
#     exit()
# else:
#     print("发送请求成功!")
#
#
#
# # urllib
# from urllib.request import  urlopen
#
#
# # 3. 接收百度服务器返回的消息;(接收数据)
# recvData = s.recv(1024*10).decode('utf-8')
#
# print("接收的页面数据为：", recvData)
# # # 4. 将获取到的网页内容保存到本文件中;
# # with open('baidu.html', 'wb') as f:
# #     print(recvData)
# s.close()