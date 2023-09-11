#!/usr/bin/python3
"""
This module contains only one function returns
True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
