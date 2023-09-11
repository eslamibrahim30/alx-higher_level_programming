#!/usr/bin/python3
"""
This module contains only one function which
returns True if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and a_class.__name__ != "object"
