import struct

# from CipherSuites import CipherSuites
# from DTLSVersion import DtlsVersion
from lib.DTLS.CipherSuites import CipherSuites
from lib.DTLS.DTLSVersion import DtlsVersion


class DTLSContext(object):
    def __init__(self, version):
        if not isinstance(version, DtlsVersion):
            raise TypeError('The version parameter must be a value of Enum DtlsVersion')
        self.version = version
        self.cipher_suites = bytearray()
        self.load_all_cipher_suites()
        self.compression_methods_length = b'\x01'  # 0x01
        self.compression_methods = b'\x00'

    def load_all_cipher_suites(self):
        for name, member in CipherSuites.__members__.items():
            self.cipher_suites.extend(struct.pack('>H', member.value))

    def set_cipher_suites(self, *args):
        self.cipher_suites = bytearray()    # Clear current cipher suite
        for cipher_suite in args:
            if not isinstance(cipher_suite, CipherSuites):
                raise TypeError('All the parameters shoud be instance of Enum CipherSuites')
            self.cipher_suites.extend(struct.pack('>H', cipher_suite))

    def get_dtls_version(self):
        return self.version

    def get_compression_methods(self):
        return self.compression_methods

    def get_cipher_suites_bytes(self):
        return bytes(self.cipher_suites)
