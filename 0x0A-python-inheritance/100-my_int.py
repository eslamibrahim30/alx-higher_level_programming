#!/usr/bin/python3
"""
This module contains only one class MyInt that inherits from int.
"""


class MyInt(int):
    """
    This class can be used as a custom int.
    MyInt has == and != operators inverted.
    """
    def __eq__(self, other):
        return super().__ne__(other)
    """
    This method inverts the usage of == sign.
    """
    def __ne__(self, other):
        return super().__eq__(other)
    """
    This method inverts the usage of != sign.
    """
