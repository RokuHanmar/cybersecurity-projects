# Written following this tutorial: https://www.youtube.com/watch?v=WGJC5vT5YJo&list=PL6gx4Cwl9DGDdduy0IPDDHYnUx66Vc4ed. I added some extra comments to test my understanding of the code
# Disclaimer: this program was made for display purposes. Packet sniffing without consent is illegal

# Import libraries. Socket is for packet handling, struct is for converting bytes to data structures, textwrap is for consistent formatting
import socket
import struct
import textwrap

def main():  # Runs forever, captures data packets, then calls the other functions to handle them
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))  # NOTE: AF_PACKET will not work on non-Linux operating systems
    while True:
        rawData, address = conn.recvfrom(65535)
        destMac, sourceMac, ethProto, data = ethernetFrame(rawData)
        print("\nEthernet frame: ")
        print("Destination: {}, Source: {}, Protocol: {}".format(destMac, sourceMac, ethProto))

# Unpack ethernet frame
def ethernetFrame(data):
    destMac, sourceMac, proto = struct.unpack('! 6s 6s H', data[:14])  # Standardise the first 14 parts of input as 6 bytes, 6 bytes, small unsigned int and store in 3 variables
    return getMacAddress(destMac), getMacAddress(sourceMac), socket.htons(proto), data[14:]

# Properly format MAC address into upper case hexadecimal as opposed to bytes 
def getMacAddress(bytesAddress):
    bytesString = map('{:02x}'.format, bytesAddress)
    return ':'.join(bytesString).upper()
    
# Unpacks IPv4 packets
def ipv4Packet(data):
    versionHeaderLength = data[0]
    version = versionHeaderLength >> 4
    headerLength = (versionHeaderLength & 15) * 4
    timeToLive, protocol, source, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, headerLength, timeToLive, protocol, ipv4(source), ipv4(target), data[headerLength:]
    
    
# Unpacks ICMP packets
def icmpPacket(data):
    icmpType, code, checksum = struct.unpack('! B B H', data[:4])
    return icmpType, code, checksum, data[4:]

# Unpacks the TCP segment
def tcpSegment(data):
    (sourcePort, destPort, sequence, acknowledgement, offsetReservedFlags) = struct.unpack('! H H L L H', data[:14])
    offset = (offsetReservedFlags >> 12) * 4
    flagUrg = (offsetReservedFlags & 32) >> 5
    flagAck = (offsetReservedFlags & 16) >> 4
    flagPsh = (offsetReservedFlags & 8) >> 3
    flagRst = (offsetReservedFlags & 4) >> 2
    flagSyn = (offsetReservedFlags & 2) >> 1
    flagFin = offsetReservedFlags & 1
    
    return sourcePort, destPort, sequence, acknowledgement, flagUrg, flagAck, flagPsh, flagRst, flagSyn, flagFin, data[offset:]

# Call main function
main()
