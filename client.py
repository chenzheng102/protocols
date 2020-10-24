#-*- coding:utf-8 -*-
import socket
import time

from config import server_port, server_host
# from lib.stun.stun_encode import pkt
from lib.rtcp.rtcp_encode import generateRR
from lib.rtp.rtp_encode import rtp_packets
import gevent
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = server_host,server_port
pkt = rtp_packets
print(pkt)
pkt = b'\x81\xc9\x00\x07\x00\x00\xf0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01'
sock.connect(addr)
sock.send([b'16feff000000000000000000cd010000c100000000000000c1feff24dc8f65fb5970f29af7f330b6a00942d71783db3230cba5bdb98213efdbb99f0000004ec014c00a0039003800880087c00fc00500350084c013c00900330032009a009900450044c00ec004002f009600410007c012c00800160013c00dc003000a001500120009001400110008000600ff01000049000b000403000102000a00340032000e000d0019000b000c00180009000a00160017000800060007001400150004000500120013000100020003000f0010001100230000000f000101'][0])


# def handle_request():
#     print("jlkjsadlkfj")
#     # pass
#     while True:
#         sock.send(pkt)
#         print("jljasflk")
#
# def gevent_click():
#     pass
#     # sock.connect(addr)
#     print("jklsjaf")
#     while True:
#         # print("jlsdjfkl")
#         gevent.spawn(handle_request,pkt)
# # handle_request(pkt)
# gevent.spawn(handle_request)
# time.sleep(10)
# # while True:
# #         sock.send(pkt)
# #         print("jkljkafsl")
# # gevent_click()
# # msg,addr = sock.recvfrom(1024)
# # print(msg)