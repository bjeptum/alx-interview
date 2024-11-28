#!/usr/bin/python3
"""
Making Change module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed
    to meet a given amount total.

    Args:
        coins (int):
        total (int)

    Returns:
        int : minimum coins needed.
    """
    if total <= 0:
        return 0

    # List to store the minimum coins needed
    min_coins = [float('inf')] * (total + 1)

    # 0 coins are needed to make a total of 0
    min_coins[0] = 0

    # Loop through each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            # Update the min_coins value for this amount
            min_coins[amount] = min(min_coins[amount],
                                    min_coins[amount - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
