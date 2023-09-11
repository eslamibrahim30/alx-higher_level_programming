#!/usr/bin/python3
"""
This module contains only one function returns if the object
is an instance of a class that inherited from, the specified class.
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object is an instance of a class
    that inherited from, the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
