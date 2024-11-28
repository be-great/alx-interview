#!/usr/bin/python3

"""
 0. Change comes from within
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total

    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1

    coins is a list of the values of the
    coins in your possession The value of
    a coin will always be an integer greater than 0
    You can assume you have an infinite number of
    each denomination of coin in the list
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    number_of_coins_needed = 0
    # sorted from biggest to the lestest
    coins = sorted(coins)[:: -1]
    for coin in coins:
        while coin <= total:
            total -= coin
            number_of_coins_needed += 1
        if (total == 0):
            return number_of_coins_needed
    return -1
