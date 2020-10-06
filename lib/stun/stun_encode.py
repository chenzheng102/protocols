#-*- coding:utf-8 -*-
'''

资料：https://forum.huawei.com/enterprise/en/stun-requests-and-responses/thread/551203-100289
'''
import struct,os
import binascii
MAGIC_COOKIE = 0x2112a442  # defined by the STUN standard, not a secret
# STUN request types
BIND_REQUEST = 0x0001
BIND_INDICATION = 0x0011
BIND_SUCCESS = 0x0101
BIND_ERROR = 0x0111

# STUN tag:value attributes
ATTR_MASK = 0x07ff
ATTR_MAPPED_ADDRESS = 0x0001
ATTR_USERNAME = 0x0006
ATTR_MESSAGE_INTEGRITY = 0x0008
ATTR_ERROR_CODE = 0x0009
ATTR_UNKNOWN_ATTRIBUTES = 0x000a
ATTR_REALM = 0x0014
ATTR_NONCE = 0x0015
ATTR_XOR_MAPPED_ADDRESS = 0x0020
ATTR_SOFTWARE = 0x8022
ATTR_ALTERNATE_SERVER = 0x8023
ATTR_FINGERPRINT = 0x8028
def _EncodeAttr(attrtype, value):
  print(attrtype,value)
  value = str(value)
  pkt = struct.pack('!HH', attrtype, len(value)) + value
  while (len(pkt) % 4) != 0:  # 32-bit alignment
    pkt += '\0'
  return pkt

def _Encode(msgtype, transaction_id, *attrs):
  """Encode message type, transaction id, and attrs into a STUN message."""
  transaction_id = str(transaction_id)
  if len(transaction_id) != 12:
    raise ValueError('transactionid %r must be exactly 12 bytes'
                     % transaction_id)
  print(attrs)
  for attrtype, attrval in attrs:
    print(attrtype,attrval)

  attrtext = ''.join(_EncodeAttr(attrtype, attrval)
                     for attrtype, attrval in attrs)
  pkt = (struct.pack('!HHI', msgtype, len(attrtext), MAGIC_COOKIE) +
         transaction_id +
         attrtext)
  return pkt

# print(ATTR_USERNAME)
# for attrtype, attrval in ((ATTR_FINGERPRINT,'aksdjfklds'),(ATTR_USERNAME,'aksdjfklds')):
#   print(attrtype,attrval)

transaction_id = os.urandom(12)
pkt = _Encode(BIND_REQUEST, transaction_id,
              (ATTR_MAPPED_ADDRESS,'aksdjfklds'),
              (ATTR_USERNAME,'aksdjfklds'),
               (ATTR_MESSAGE_INTEGRITY, 'aksdjfklds'),
                (ATTR_ERROR_CODE, 'aksdjfklds'),
                 (ATTR_UNKNOWN_ATTRIBUTES, 'aksdjfklds'),
              (ATTR_REALM, 'aksdjfklds'),
              (ATTR_NONCE, 'aksdjfklds'),
              (ATTR_XOR_MAPPED_ADDRESS, 'aksdjfklds'),
              (ATTR_SOFTWARE, 'aksdjfklds'),

              (ATTR_ALTERNATE_SERVER, 'aksdjfklds'),
              (ATTR_FINGERPRINT, 'aksdjfklds')

              )

ATTR_REALM = 0x0014
ATTR_NONCE = 0x0015
ATTR_XOR_MAPPED_ADDRESS = 0x0020
ATTR_SOFTWARE = 0x8022
ATTR_ALTERNATE_SERVER = 0x8023
ATTR_FINGERPRINT = 0x8028
# print(len(pkt))
