# Written following this tutorial: https://www.youtube.com/watch?v=WGJC5vT5YJo&list=PL6gx4Cwl9DGDdduy0IPDDHYnUx66Vc4ed. I added some extra comments to test my understanding of the code
# Designed for Linux systems. Designed with sudo in mind
# Disclaimer: this program was made for display purposes. Packet sniffing without consent is illegal

# Import libraries. Socket is for packet handling, struct is for converting bytes to data structures, textwrap is for consistent formatting
import socket
import struct
import textwrap

def main():  # Runs forever, captures data packets, then calls the other functions to handle them
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))  # NOTE: AF_PACKET will not work on non-Linux operating systems
    while True:
        rawData, address = connection.recvfrom(65535)
        destMac, sourceMac, ethProto, data = ethernetFrame(rawData)
        print("\nEthernet frame: ")
        print("Destination: {}, Source: {}, Protocol: {}".format(destMac, sourceMac, ethProto))
        
        if ethProto == 8:  # 8 represents IPv4
            (version, headerLength, timeToLive, protocol, source, target, data) = ipv4Packet(data)
            print("IPv4 Packet:")
            print("Version: {}, Header Length: {}, Time to Live: {}".format(version, headerLength, timeToLive))
            print("Protocol: {}, Source: {}, Target: {}".format(protocol, source, target))
            
            if protocol == 1:  # 1 represents ICMP
                (icmpType, code, checksum, data) = icmpPacket(data)
                print("ICMP Packet:")
                print("ICMP Type: {}, Code: {}, Checksum: {}".format(icmpType, code, checksum))
                print("Data: {}".format(data))
                
            elif protocol == 6:  # 6 represents TCP
                (sourcePort, destPort, sequence, acknowledgement, offsetReservedFlags, data) = tcpSegment(data)
                print("TCP Segment:")
                print("Source Port: {}, Destination Port: {}, Sequence: {}".format(sourcePort, destPort, sequence))
                print("Acknowledgement: {}, Offset Reserved Flags: {}".format(acknowledgement, offsetReservedFlags))
                print("Data: {}".format(data))
                
            elif protocol == 17:  # 17 represents UDP
                (sourcePort, destPort, size, data) = udpPacket(data)
                print("UDP Packet:")
                print("Source Port: {}, Destination Port: {}, Size: {}".format(sourcePort, destPort, size))
                print("Data: {}".format(data))
                
            else:  # Error handling
                print("Data: ")
                print(formatMultiLineData(data))

        else:  # Error handling
            print("Data: ")
            print(formatMultiLineData(data))


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

# Unpacks UDP packets
def udpPacket(data):
    sourcePort, destPort, size = struct.unpack('! H H 2x H', data[:8])
    return sourcePort, destPort, size, data[8:]

# Format multiline data. 
def formatMultiLineData(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string.size)])

# Call main function
main()

""" What did I learn from this tutorial?

    1. How to use the Socket and Struct libraries
    2. The way Windows and Linux handle networks is different
    3. Following on from point 2, that specific Python commands will not work on certain operating systems
    4. How to use the .format command to inline variables the way they're inlined in C
    5. How to inline a for loop
"""
