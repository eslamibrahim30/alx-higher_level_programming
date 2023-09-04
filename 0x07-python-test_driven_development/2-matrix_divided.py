#!/usr/bin/python3
"""
This module contains a function which divides
all elements of a matrix by a given number.
After that it returns the new matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a number
    """
    is_matrix = 1
    if matrix is None or len(matrix) == 0:
        is_matrix = 0
    if type(matrix) is not list:
        is_matrix = 0
    for row in matrix:
        if type(row) is not list:
            is_matrix = 0
    for row in matrix:
        for e in row:
            if type(e) not in [int, float]:
                is_matrix = 0
    if is_matrix == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(row_len):
            new_row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_row)
    return new_matrix
