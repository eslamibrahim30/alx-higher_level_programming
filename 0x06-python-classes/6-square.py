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
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if not isinstance(position, tuple) and len(position) == 2:
            raise TypeError('position must be a tuple of 2 positive integers')
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
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    """
    This class method is used to set the __size attribute
    by a given value
    Args:
        value: the given value
    """
    def my_print(self):
        max_space = 0
        if not self__position is None:
            if self.__position[0] > self.__position[1]:
                max_space = self.__position[0]
            else:
                max_space = self.__position[1]
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(max_space):
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
        if not isinstance(value, tuple) and len(value) == 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
    """
    This class method is used to set the __position attribute
    by a given value.
    Args:
        value: the given value of the position
    """
