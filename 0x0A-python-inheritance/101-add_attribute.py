#!/usr/bin/python3
"""
This module contains only one function that
adds a new attribute to an object if it’s possible.
"""


def add_attribute(obj, name, value):
    """
    This function adds a new attribute to an object if it’s possible.
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
