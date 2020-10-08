# -*- coding: utf-8 -*-

from gevent import monkey

from config import server_host, server_port
import socket

from lib.rtcp.rtcp_encode import generateRR
from lib.rtp.rtp_encode import rtp_packets

monkey.patch_all()
import gevent
import requests
from datetime import datetime

def socket_test(n=1000):
    print("n--->",n)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = server_host, server_port
    # pkt=[b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'][0]
    pkt = rtp_packets
    print(pkt)
    pkt = b'\x81\xc9\x00\x07\x00\x00\xf0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01'
    sock.connect(addr)
    # sock.send(generateRR())
    # while True:
    for i in range(int(n)):
        sock.send(generateRR())
        print("jkljlksdaf")
    # gevent.spawn(socket_test,sock)


def handles_request(sock):

    while True:
        sock.send(generateRR())

# socket_test()
gevent.spawn(socket_test,1000)
gevent.spawn(socket_test,1000)

# gevent.spawn(f,"http://www.baidu.com")