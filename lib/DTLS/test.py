import socket

# from DTLSVersion import DtlsVersion
# from DTLSContext import DTLSContext
# from DtlsConnection import DTLSConnection
from lib.DTLS.DTLSContext import DTLSContext
from lib.DTLS.DTLSVersion import DtlsVersion

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = '127.0.0.1'
port = 1106

ctx = DTLSContext(DtlsVersion.DTLSv12)
# dtls_connection = DTLSConnection(s, ctx, ip, port)
# dtls_connection.do_handshake()
