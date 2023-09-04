#!/usr/bin/python3
"""
This module contains a Rectangle class.
"""


class Rectangle:
    """
    This class doesn't do anything until now
    """
    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width
    """
    This class method initializes an inistance of the class
    """
    @property
    def height(self):
        return self.__height
    """
    This class method retrieves the value of height attribute.
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
    """
    This class method sets height attribute with a given value.
    """
    @property
    def width(self):
        return self.__width
    """
    This class method retrieves the value of width attribute.
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
    """
    This class method sets width attribute with a given value.
    """
    def area(self):
        return self.__height * self.__width
    """
    This class method calculates the area of the rectangle.
    """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
    """
    This class method calculates the perimeter of the rectangle.
    """
