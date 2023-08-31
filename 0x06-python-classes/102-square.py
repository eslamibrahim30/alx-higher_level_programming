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
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    """
    This class method initializes an inistance of the class
        Args:
            size: the size of the square
    """
    def area(self):
        return self.__size ** 2
    """
    This class method calculates the area of the square
    """
    @property
    def size(self):
        return self.__size
    """
    This class method is used to retrieve the __size attribute
    Returns:
        the size value of the square object
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    """
    This class method is used to set the __size attribute
    by a given value
    Args:
        value: the given value
    """
    def __eq__(self, other):
        return self.area() == other.area()
    """
    This is an operator overloading for the == sign
    """
    def __ne__(self, other):
        return self.area() != other.area()
    """
    This is an operator overloading for the != sign
    """
    def __gt__(self, other):
        return self.area() > other.area()
    """
    This is an operator overloading for the > sign
    """
    def __ge__(self, other):
        return self.area() >= other.area()
    """
    This is an operator overloading for the >= sign
    """
    def __lt__(self, other):
        return self.area() < other.area()
    """
    This is an operator overloading for the < sign
    """
    def __le__(self, other):
        return self.area() <= other.area()
    """
    This is an operator overloading for the <= sign
    """
