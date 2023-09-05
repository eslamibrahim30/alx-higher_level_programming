#!/usr/bin/python3
"""
This module contains a Rectangle class.
"""


class Rectangle:
    """
    This class doesn't do anything until now
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height
        Rectangle.number_of_instances += 1
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
    def __str__(self):
        out = ""
        for i in range(self.__height):
            for j in range(self.__width):
                out += str(self.print_symbol)
            if i != self.__height - 1:
                out += "\n"
        return out
    """
    This class method provides the informal string representation of
    the rectangle, aimed at the user.
    """
    def __repr__(self):
        return "{}({}, {})".format(
                type(self).__name__, self.__width, self.__height)
    """
    This class method provides the official string representation of
    the rectangle, aimed at the programmer.
    """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    """
    This class method prints "Bye rectangle..." when
    an instance of Rectangle is deleted.
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
    """
    This static method compares two rectangles based on their areas
    and return the rectangle with the bigger area.
    """
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
    """
    This class method returns a new Rectangle instance
    with width == height == size
    """
