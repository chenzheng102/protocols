#-*- coding:utf-8 -*-
#-*- coding:utf-8 -*-
import socket
from config import server_port, server_host
#构建RTP协议报文
'''
RTP 报文结构：
    header+有效负载
    
RTP header:
    version 2 bit
    padding 1 bit
    extension 1 bit
    CSRC count 4 bit
    
    
    marker 1bit
    payload type 7 bit
    
    sequence number: 16 bit
    timestamp: 32 bit
    SSRC: 32 bit
    
有效负载：payload

1 bits = 8 bit
'''
#one->v0 v1 p2 x3 c4 c5 c6 c7
version = 2
padding = 0
x = 0
cc =0
one = (version<<6)|(padding<<5)|(x<<4)|cc
#two->m0 p1 p2 p3 p4 p5 p6 p7
marker = 0
pt = 127 # 0~127
two = (marker<<7)|pt
import struct
sequence_number = 0
timestamp = 0
ssrc = 0
body = struct.pack(">BBHII",one,two,sequence_number,timestamp,ssrc) #打包成二进制
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #udp协议
addr = server_host,server_port

sock.connect(addr)
sock.send(body)
