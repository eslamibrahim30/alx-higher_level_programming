#!/usr/bin/python3
"""
This module for task "7. Lazy matrix multiplication".
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if not isinstance(j, float) and not isinstance(j, int) or j != j:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if not isinstance(j, float) and not isinstance(j, int) or j != j:
                raise TypeError("m_b should contain only integers or floats")
    w_a = len(m_a[0])
    h_a = 0
    for i in m_a:
        h_a += 1
        if len(i) != w_a:
            raise TypeError("each row of m_a must be of the same size")
    w_b = len(m_b[0])
    h_b = 0
    for i in m_b:
        h_b += 1
        if len(i) != w_b:
            raise TypeError("each row of m_b must be of the same size")
    if w_a != h_b:
        raise ValueError("m_a and m_b can't be multiplied")
    mat_a = np.matrix(m_a)
    mat_b = np.matrix(m_b)
    result = mat_a * mat_b
    return result
