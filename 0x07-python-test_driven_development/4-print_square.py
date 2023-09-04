#!/usr/bin/python3
"""
This module contains only one function
which prints a square using the '#' char
followed by a new line.
"""


def print_square(size):
    """
    This function prints a square using #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
