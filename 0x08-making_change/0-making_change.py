#!/usr/bin/python3

"""
    This module contians a funtion that determines
    feswest number of coins to make `total`
"""


def makeChange(coins, total):
    """
       This function calculates the fewest number
       of coins to make total.
       Args:
           coins(list):list of the values of the coins in your possession
           total(int): number of total coins.
       Returns:
           if total is 0 or less, return 0.
           if total cannot be met by any number of coins you have.
              return -1
    """

    if total <= 0:
        return 0

    coin_piles = [float('inf')] * (total + 1)

    coin_piles[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            coin_piles[x] = min(coin_piles[x], coin_piles[x - coin] + 1)

    return coin_piles[total] if coin_piles[total] != float('inf') else -1
