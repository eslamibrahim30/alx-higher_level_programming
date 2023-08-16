#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    res = [list(map(lambda x: x**2, matrix[i])) for i in range(len(matrix))]
    return res
