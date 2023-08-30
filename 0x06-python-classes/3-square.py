#!/usr/bin/python3
"""
This module contains a class to define a square
"""


class Square():
    """
    This class is used to define an instance
    of a square object
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise Exception('size must be an integer')
        if size < 0:
            raise Exception('size must be >= 0')
        self.__size = size
    """
    This class method initializes an inistance of the class
        Args:
            size: the size of the square
    """
    def area(self):
        return self.__size ** 2
    """
    The class method calculates the area of the square
    """
