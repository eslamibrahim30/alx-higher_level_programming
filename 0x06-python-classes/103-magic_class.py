#!/usr/bin/python3
"""
This module contains a magic class for a circle
"""


class MagicClass():
    """
    This is a magic class for a circle
    It is used to create an instance of a circle in our program
    """
    def __init__(self, raduis=0):
        if  type(raduis) is not int and type(raduis) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__raduis = raduis
    """
    This class method initializes an inistance of the class.
    Args:
        raduis: the raduis of the circle.
    """
    def area(self):
        return (self.__raduis ** 2) * math.pi
    """
    This class method calculates the area of the circle.
    """
    def circumference(self):
        return 2 * math.pi * self.__raduis
    """
    This class method calculates the circumference of the circle.
    """
