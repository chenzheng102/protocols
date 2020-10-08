#-*- coding:utf-8 -*-
#https://github.com/qichengyue/pyDtlsLib
import socket
import struct

from lib.DTLS.DTLSContext import DTLSContext
from lib.DTLS.DTLSVersion import DtlsVersion
from lib.DTLS.Record import ClientHello
# from .DtlsConnection import DTLSConnection

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = '127.0.0.1'
port = 1106
ctx = DTLSContext(DtlsVersion.DTLSv12)
# dtls_connection = DTLSConnection(s, ctx, ip, port)
# dtls_connection.do_handshake()
client_hello = ClientHello(ctx)
ba = bytearray()
print([ba])
ba.extend(client_hello.get_record_bytes())
print("2020", [ba])
print("2020", [ba[-2:]], [struct.pack('>H', len(client_hello.get_payload_bytes()))])
ba[-2:] = struct.pack('>H', len(client_hello.get_payload_bytes()))  # fill up length segment
print(ba)
ba.extend(client_hello.get_payload_bytes())

from config import server_port, server_host
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = server_host,server_port
# pkt=[b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'][0]
# pkt = rtp_packets
# print(pkt)
# # pkt = b'\x81\xc9\x00\x07\x00\x00\xf0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01'
sock.connect(addr)
print(ba)
sock.send(bytes(ba))