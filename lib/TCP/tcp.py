#-*- coding:utf-8 -*-
'''
https://harttle.land/2014/09/27/tcp.html
https://tools.ietf.org/html/rfc793

Transmission Control Protocol, Src Port: 60504, Dst Port: 443, Seq: 1, Ack: 38, Len: 0
    Source Port: 60504
    Destination Port: 443
    [Stream index: 0]
    [TCP Segment Len: 0]
    Sequence number: 1    (relative sequence number)
    Sequence number (raw): 1706462680
    [Next sequence number: 1    (relative sequence number)]
    Acknowledgment number: 38    (relative ack number)
    Acknowledgment number (raw): 1876756339
    1000 .... = Header Length: 32 bytes (8)
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ·······A····]
    Window size value: 32767
    [Calculated window size: 32767]
    [Window size scaling factor: -1 (unknown)]
    Checksum: 0xed43 [unverified]
    [Checksum Status: Unverified]
    Urgent pointer: 0
    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
        TCP Option - No-Operation (NOP)
            Kind: No-Operation (1)
        TCP Option - No-Operation (NOP)
        TCP Option - Timestamps: TSval 797134818, TSecr 1822605653
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 1]
        [The RTT to ACK the segment was: 0.000082000 seconds]
    [Timestamps]
        [Time since first frame in this TCP stream: 0.000082000 seconds]
        [Time since previous frame in this TCP stream: 0.000082000 seconds]

'''
SourcePort = 60504
DestinationPort=443
SequenceNumber =1
AcknowledgmentNumber=38
DataOffset=0
Reserved=0x4000
ControlBits=0
Window = 0
Checksum =0
UrgentPointer=0
Options=0
Padding = 0
data=0

import struct
header = struct.pack(">HHII",SourcePort,DestinationPort,SequenceNumber,AcknowledgmentNumber)
#-> o0 01 02 03
one = (DataOffset<<4)|Reserved
#->

print(len(header))