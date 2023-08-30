#!/usr/bin/python3
"""
This module contains a class to define a square
"""


class Square():
    """
    This class is used to define an instance
    of a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if (
                not isinstance(position, tuple) or
                not len(position) == 2 or
                not isinstance(position[0], int) or
                not isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position
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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    """
    This class method is used to set the __size attribute
    by a given value
    Args:
        value: the given value
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
    """
    This class method prints in stdout the square with the character #
    """
    @property
    def position(self):
        return self.__position
    """
    This class method is used to retrive the __position attribute
    Returns:
        the current position in the square.
    """
    @position.setter
    def position(self, value):
        if (
                not isinstance(position, tuple) or
                not len(position) == 2 or
                not isinstance(position[0], int) or
                not isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position
    """
    This class method is used to set the __position attribute
    by a given value.
    Args:
        value: the given value of the position
    """
