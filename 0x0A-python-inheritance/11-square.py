#!/usr/bin/python3
"""
This module contains only one class defined as Square class,
This class inherits from Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class is used to define a square.
    """
    def __init__(self, size):
        if Rectangle.integer_validator(self, "size", size):
            super().__init__(size, size)
            self.__size = size
    """
    This method initializes a given instance of the Square class.
    """
    def area(self):
        return self.__size ** 2
    """
    This method returns a string representtion of the Square.
    """
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
    """
    This method returns a string representtion of the Square.
    """
