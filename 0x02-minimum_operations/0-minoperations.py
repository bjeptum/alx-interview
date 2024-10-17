#!/usr/bin/python3
"""
Minimum Copy Paste Operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to achieve
    exactly n 'H' characters in a text file
    using Copy All and Paste operations.
    """
    if n <= 1:
        return 0
    res = 0  # Holds the total count of operations
    i = 2  # Start checking factors from 2

    # Check factors up to n
    while i <= n:
        while n % i == 0:  # While i is a factor of n
            res += i  # Add to total count
            n = n // i  # Divide n by the factor
        i += 1  # Move to next

    if n > 1:
        res += n

    return res
