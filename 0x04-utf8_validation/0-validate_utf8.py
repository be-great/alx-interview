#!/usr/bin/python3
"""
A method that determines if a given
data set represents a valid UTF-8
encoding.
"""


def validUTF8(data):
    """
    Validates if the given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0
    for byte in data:
        # Get the binary representation of the byte, padded to 8 bits
        byte_bin = format(byte, '08b')

        if num_bytes == 0:
            if byte_bin.startswith('0'):  # 1-byte character
                num_bytes = 0
            elif byte_bin.startswith('110'):  # 2-byte character
                num_bytes = 1
            elif byte_bin.startswith('1110'):  # 3-byte character
                num_bytes = 2
            elif byte_bin.startswith('11110'):  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid starting byte
        else:
            # Expecting a continuation byte
            if not byte_bin.startswith('10'):
                return False  # Invalid continuation byte
            num_bytes -= 1
    return num_bytes == 0  # Ensure all characters were complete
