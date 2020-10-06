#-*- coding:utf-8 -*-
import socket

from protocol.config import server_host, server_port

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,  1 )
addr = server_host,server_port
sock.bind(addr)
# sock.listen(2)
print("start server---->")
while True:
    # msg ,addr = sock.recvfrom(1024)
    message, address = sock.recvfrom(8192)
    print(message,address)
    sock.sendto(message,address)
    # print(msg)
