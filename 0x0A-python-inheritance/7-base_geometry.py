#!/usr/bin/python3
"""
This module contains only one class which can be used
to calculate basic geometry formulas.
"""


class BaseGeometry:
    """
    This class is used to do geometric calculations.
    """
    def area(self):
        raise Exception("area() is not implemented")
    """
    This method should calculates the area of a given object.
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
    """
    This method validates if a given value is a positive integer value.
    """
