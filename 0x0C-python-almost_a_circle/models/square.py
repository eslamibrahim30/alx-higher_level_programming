#!/usr/bin/python3
"""
This module Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class for creating a Square object.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This method initializes each attribute in a Square object.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        This class method is used to retrieve the __width attribute
        Returns:
            the width value of a Square object
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        This class method is used to set the __width attribute
        by a given value.
        Args:
            size: the given value of the size of the square
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
        This class method returns the string representation of
        a square.
        """
        rect_str = "[Square] "
        rect_str += "({}) {}/{} ".format(self.id, self.x, self.y)
        rect_str += "- {}".format(self.width)
        return rect_str

    def update(self, *args, **kwargs):
        """
        This class method assigns an argument to each attribute
        of the Square object.
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        This class method returns the dictionary representation of a Square.
        """
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['size'] = self.size
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict
