'''
https://github.com/gabrieljablonski/rtsp-rtp-stream/blob/master/src/utils/rtp_packet.py

'''
VERSION = 2
PADDING = 0
EXTENSION = 0
CC = 0
MARKER = 0
payload = 0

payload_type = 127
sequence_number = 0
timestamp = 0
SSRC = 000
# b0 -> v0 v1 p x c0 c1 c2 c3
zeroth_byte = (VERSION << 6) | (PADDING << 5) | (EXTENSION << 4) | CC
# b1 -> m pt0 pt1 pt2 pt3 pt4 pt5 pt6
first_byte = (MARKER << 7) | payload_type
# b2 -> s0 s1 s2 s3 s4 s5 s6 s7
second_byte = sequence_number >> 8
# b3 -> s8 s9 s10 s11 s12 s13 s14 s15
third_byte = sequence_number & 0xFF
# b4~b7 -> timestamp
fourth_to_seventh_bytes = [
	(timestamp >> shift) & 0xFF for shift in (24, 16, 8, 0)
]
# b8~b11 -> ssrc
eigth_to_eleventh_bytes = [
	(SSRC >> shift) & 0xFF for shift in (24, 16, 8, 0)
]
header = bytes((
	zeroth_byte,
	first_byte,
	second_byte,
	third_byte,
	*fourth_to_seventh_bytes,
	*eigth_to_eleventh_bytes,
))


rtp_packets = header+bytes(payload)
# print(bytes((
# 	zeroth_byte,
# 	first_byte,
# 	second_byte,
# 	third_byte,
# 	*fourth_to_seventh_bytes,
# 	*eigth_to_eleventh_bytes,
# )))