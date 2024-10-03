#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Return a Pascal's triangle of n."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    tri = []

    for row in range(n):
        current_row = [1]
        if row > 0:
            for colum in range(1, row):
                value = tri[row - 1][colum - 1] + tri[row - 1][colum]
                current_row.append(value)
            current_row.append(1)

        tri.append(current_row)

    return tri
