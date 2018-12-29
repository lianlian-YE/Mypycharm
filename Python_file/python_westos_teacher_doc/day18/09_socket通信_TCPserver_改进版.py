#!/usr/bin/env python
#coding:utf-8


""""
Name: 09_socket通信_TCPserver_改进版.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import os
import socket

HOST = '172.25.254.250'
PORT = 9881

# 1. 创建服务端的socket对象
with socket.socket() as serverSocket:
    # 2. 绑定一个ip和端口， 客户端连接时的socket；
    serverSocket.bind((HOST, PORT))
    # 3. 一直监听是否有客户端连接
    serverSocket.listen()
    print("server is listening %d......." %(PORT))
    # 4. 如果有客户端连接, 接收客户端的连接;
    # serverSocket.accept会返回2个值, address指的是， 客户端的ip和端口;
    clientSocket, address = serverSocket.accept()

    with clientSocket:
        while True:
            # 5. 客户端和服务端进行通信;
            cmd = clientSocket.recv(1024).decode('utf-8')
            # 执行客户端发送的命令;
            """
            执行linux命令:
                1. 如果想获取命令是否执行成功? os.systemc('cmd')
                        返回为0: 代表成功
                        返回为非0， 代表失败;
            
                2. 如果想获取命令的执行结果,可以保存到变量中 os.popen(cmd)
            """

            if os.system(cmd) == 0:
                resData = os.popen(cmd).read()
                if resData:
                    resData = resData.encode('utf-8')
                    # 6. 给客户端回复消息
                    clientSocket.send(resData)
                else:
                    print("no response.")

            else:
                print("命令执行失败!")



