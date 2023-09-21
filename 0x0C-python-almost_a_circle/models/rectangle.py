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
        """
        This method initializes each attribute in a Rectangle object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        This class method is used to retrieve the __width attribute
        Returns:
            the width value of a Rectangle object
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        This class method is used to set the __width attribute
        by a given value.
        Args:
            width: the given value of width
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """
        This class method is used to retrieve the __height attribute
        Returns:
            the height value of a Rectangle object
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        This class method is used to set the __height attribute
        by a given value.
        Args:
            height: the given value of height
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """
        This class method is used to retrieve the __x attribute
        Returns:
            the x value of a Rectangle object
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        This class method is used to set the __x attribute
        by a given value.
        Args:
            x: the given value of x
        """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """
        This class method is used to retrieve the __y attribute
        Returns:
            the y value of a Rectangle object
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        This class method is used to set the __y attribute
        by a given value.
        Args:
            y: the given value of y
        """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """
        This class method calculates the area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """
        This class method prints in stdout the Rectangle instance
        with the character #.
        """
        my_display = ""
        for i in range(self.y):
            my_display += "\n"
        for i in range(self.height):
            for j in range(self.x):
                my_display += " "
            for j in range(self.width):
                my_display += "#"
            if i < self.height - 1:
                my_display += "\n"
        print(my_display)
        return my_display

    def __str__(self):
        """
        This class method returns the string representation of
        a rectangle.
        """
        rect_str = "[Rectangle] "
        rect_str += "({}) {}/{} ".format(self.id, self.x, self.y)
        rect_str += "- {}/{}".format(self.width, self.height)
        return rect_str

    def update(self, *args, **kwargs):
        """
        This class method assigns an argument to each attribute
        of the Rectangle object.
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        This class method returns the dictionary representation of a Rectangle.
        """
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.width
        rect_dict['height'] = self.height
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict
