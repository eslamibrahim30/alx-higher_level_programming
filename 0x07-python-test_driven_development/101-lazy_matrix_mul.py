#!/usr/bin/python3
"""
This module for task "7. Lazy matrix multiplication".
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices.
    """
    mat_a = np.array(m_a)
    mat_b = np.array(m_b)
    return np.matmul(mat_a, mat_b)
