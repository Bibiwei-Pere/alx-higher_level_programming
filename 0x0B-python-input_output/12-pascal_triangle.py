#!/usr/bin/python3

"""
This module contains a function that returns a pascal's triangle
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing
    pascal's triangle

    Args:
        n: length of the triangle
    """
    if n <= 0:
        return []
    else:
        rows = [[1] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                try:
                    prev = rows[i - 1][j + 1]
                except IndexError:
                    prev = 0
                rows[i].append(prev + rows[i-1][j])
        return rows
