#!/usr/bin/python3
"""
This module for Rectangle class.
"""
from models.base import Base

class Rectangle(Base):
    """
    This class for creating a Rectangle object.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    """
    This method initializes each attribute in a Rectangle object.
    """
    @property
    def width(self):
        return self.__width
    """
    This class method is used to retrieve the __width attribute
    Returns:
        the width value of a Rectangle object
    """
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
    """
    This class method is used to set the __width attribute
    by a given value.
    Args:
        width: the given value of width
    """
    @property
    def height(self):
        return self.__height
    """
    This class method is used to retrieve the __height attribute
    Returns:
        the height value of a Rectangle object
    """
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
    """
    This class method is used to set the __height attribute
    by a given value.
    Args:
        height: the given value of height
    """
    @property
    def x(self):
        return self.__x
    """
    This class method is used to retrieve the __x attribute
    Returns:
        the x value of a Rectangle object
    """
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
    """
    This class method is used to set the __x attribute
    by a given value.
    Args:
        x: the given value of x
    """
    @property
    def y(self):
        return self.__y
    """
    This class method is used to retrieve the __y attribute
    Returns:
        the y value of a Rectangle object
    """
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y
    """
    This class method is used to set the __y attribute
    by a given value.
    Args:
        y: the given value of y
    """
    def area(self):
        return self.__height * self.__width
    """
    This class method calculates the area of the rectangle.
    """
    def display(self):
        my_display = ""
        for i in range(self.height):
            for j in range(self.width):
                my_display += "#"
            if i < self.height - 1:
                my_display += "\n"
        print(my_display)
        return my_display
    """
    This class method prints in stdout the Rectangle instance
    with the character #.
    """
