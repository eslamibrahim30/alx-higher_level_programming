#!/usr/bin/python3
"""
This module for Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []
    my_tri = [[1]]
    for i in range(1, n):
        new_row = []
        for j in range(i + 1):
            new_row.append(0)
            if j - 1 >= 0:
                new_row[j] += my_tri[i - 1][j - 1]
            if j < i:
                new_row[j] += my_tri[i - 1][j]
        my_tri.append(new_row)
    return my_tri
