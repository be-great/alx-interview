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
        # Ensure the byte is in the valid range of 0 to 255
        if byte < 0 or byte > 255:
            return False
        # Check how many bytes this character should have
        if num_bytes == 0:
            if (byte >> 7) == 0b0:  # 1-byte character
                num_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid starting byte
        else:
            # Expecting a continuation byte
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1

    return num_bytes == 0  # Ensure all characters were completed
