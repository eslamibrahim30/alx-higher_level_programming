#!/usr/bin/python3
"""
This module contains only one class which is defined as Rectangle class,
This class inherits from BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class is used to define a rectangle.
    """
    def __init__(self, width, height):
        if (BaseGeometry.integer_validator(self, "width", width)):
            self.__width = width
        if (BaseGeometry.integer_validator(self, "height", height)):
            self.__height = height
    """
    This method initializes a given instance of the Rectangle class.
    """
    def area(self):
        return self.__height * self.__width
    """
    This method calculates the area of the Rectangle.
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    """
    This method returns a string representtion of the Rectangle.
    """
