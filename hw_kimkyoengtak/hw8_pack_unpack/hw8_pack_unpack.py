# python3 hw8_pack_unpack.py

from socket import *
import struct, binascii

# pack => 값을 바이트(bytes)로 바꾸는 것
# data = struct.pack('!HH', 1234, 5678)
# print(data)  # b'\x04\xd2\x16.'

# unpack => 바이트를 다시 원래 값(숫자 등)으로 바꾸는 것
# data = b'\x04\xd2\x16.'
# values = struct.unpack('!HH', data)
# print(values)  # (1234, 5678)

class Udphdr:
    def __init__(self, source_port, destination_port, length, checksum):
        self.source_port = source_port
        self.destination_port = destination_port
        self.length = length
        self.checksum = checksum
        
    def pack_Udphdr(self):
        return struct.pack('!4H', self.source_port, self.destination_port, self.length, self.checksum)
        
    def unpack_Udphdr(self, buffer):
        return struct.unpack('!4H', buffer[:8])
        
    def getSrcPort(self, unpacked):
        return unpacked[0]
    
    def getDstPort(self, unpacked):
        return unpacked[1]
    
    def getLength(self, unpacked):
        return unpacked[2]
    
    def getChecksum(self, unpacked):
        return unpacked[3]
        
if __name__ == '__main__':
    
    udp = Udphdr(5555, 80, 1000, 0xFFFF)

    packed_udphdr = udp.pack_Udphdr()
    print(binascii.b2a_hex(packed_udphdr))

    unpacked_udphdr = udp.unpack_Udphdr(packed_udphdr)
    print(unpacked_udphdr)

    print(f'Source Port:{udp.getSrcPort(unpacked_udphdr)} Destination Port:{udp.getDstPort(unpacked_udphdr)} Length:{udp.getLength(unpacked_udphdr)} Checksum:{udp.getChecksum(unpacked_udphdr)}')