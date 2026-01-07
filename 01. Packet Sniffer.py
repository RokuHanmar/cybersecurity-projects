# Written following this tutorial: https://www.youtube.com/watch?v=WGJC5vT5YJo&list=PL6gx4Cwl9DGDdduy0IPDDHYnUx66Vc4ed. I added some extra comments to test my understanding of the code

# Import libraries. Socket is for packet handling, struct is for converting bytes to data structures, textwrap is for consistent formatting
import socket
import struct
import textwrap

# Unpack ethernet frame
def ethernetFrame(data):
    destMac, sourceMac, proto = struct.unpack('! 6s 6s H', data[:14])  # Standardise the first 14 parts of input as 6 bytes, 6 bytes, small unsigned int and store in 3 variables
    return getMacAddress(destMac), getMacAddress(sourceMac), socket.htons(proto), data[14:]

# Properly format MAC address into upper case hexadecimal as opposed to bytes
def getMacAddress(bytesAddress):
    bytesString = map('{:02x}'.format, bytesAddress)
    return ':'.join(bytesString).upper()
    
