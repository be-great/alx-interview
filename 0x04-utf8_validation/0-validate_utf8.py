#!/usr/bin/python3
"""
a method that determines if a given
data set represents a valid UTF-8
encoding.
"""


def validUTF8(data):
    """
    0. UTF-8 Validation
    """
    num_bytes = 0
    for byte in data:
        # get the binary representation of the bytes
        # padding to 8 bits
        byte_bin = format(byte, '08b')

        if num_bytes == 0:
            if byte_bin.startswith('0'):  # 1-byte character
                num_bytes = 0
            elif byte_bin.startswith('110'):  # 2-byte
                num_bytes = 1
            elif byte_bin.startswith('1110'):
                num_bytes = 2
            elif byte_bin.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            # expecting a continuation byte
            if not byte_bin.startswith('10'):
                return False
            num_bytes -= 1
    return num_bytes == 0
