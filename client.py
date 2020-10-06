#-*- coding:utf-8 -*-
import socket

from config import server_port, server_host
# from lib.stun.stun_encode import pkt
from lib.rtcp.rtcp_encode import generateRR
from lib.rtp.rtp_encode import rtp_packets

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = server_host,server_port
# pkt=[b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'][0]
pkt = rtp_packets
print(pkt)
pkt = b'\x81\xc9\x00\x07\x00\x00\xf0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01'
sock.connect(addr)
sock.send(generateRR())
# msg,addr = sock.recvfrom(1024)
# print(msg)