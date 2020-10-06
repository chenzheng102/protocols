#-*- coding:utf-8 -*-
'''
https://github.com/plazmer/pyrtsp/blob/master/rtcp_datagram.py
'''
from struct import pack

SSRC_sender = 0
NTP_TimestampH = 0
NTP_TimestampL = 0
RTP_Timestamp = 0
SenderPacketCount = 0
SenderOctetCount = 0
def generateRR(NTP_TimestampH=NTP_TimestampH,NTP_TimestampL=NTP_TimestampL,SSRC_sender=SSRC_sender,SenderPacketCount=SenderPacketCount):
    # Ver 2, Pad 0, RC 1
    Ver_P_RC = 0b10000001
    # PT 201, Length 7, SSRC 0xF00F - let it be our ID
    Header = pack('!BBHI', Ver_P_RC, 201, 7, 0x0000F00F)
    NTP_32 = (NTP_TimestampH & 0x0000FFFF) + ((NTP_TimestampL & 0xFFFF0000) >> 16)
    # No lost packets, no delay in receiving data, RR sent right after receiving SR
    # Instead of SenderPacketCount should be proper value
    ReceiverReport = pack('!IBBHIIII', SSRC_sender, 0, 0, 0, SenderPacketCount, 1, NTP_32, 1)
    return Header + ReceiverReport
