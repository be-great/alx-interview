#!/usr/bin/python3
"""
0x02. Minimum Operations
"""


def minOperations(n):
    """
    calculate the min number of operations
    """
    if n <= 1:
        return 0
    oper = 0
    div = 2
    while n > 1:
        while n % div == 0:
            oper += div
            n //= div
        div += 1
    return oper
