#-*- coding:utf-8 -*-
import socket

from config import server_port, server_host
# from lib.stun.stun_encode import pkt
from lib.rtp.rtp_encode import rtp_packets

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = server_host,server_port
# pkt=[b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'][0]
pkt = rtp_packets
print(pkt)
sock.connect(addr)
sock.send(pkt)
# msg,addr = sock.recvfrom(1024)
# print(msg)