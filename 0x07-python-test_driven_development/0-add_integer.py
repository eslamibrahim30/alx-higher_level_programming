#!/usr/bin/python3
"""
This module contains the add function
which simply adds two numbers. it converts
the two numbers before addition.
"""


def add_integer(a, b=98):
    """This function adds two numbers a and b.
    a and b must be integers or floats, otherwise raise a TypeError
    a and b must be first casted to integers if they are float."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
