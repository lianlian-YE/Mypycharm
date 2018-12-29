import socket
server=socket.socket()
server.bind(('127.0.0.1',5001))
server.listen(5)
conn,addr=server.accept()
data=conn.recv(1024)
conn.send(data.upper())
server.close()
