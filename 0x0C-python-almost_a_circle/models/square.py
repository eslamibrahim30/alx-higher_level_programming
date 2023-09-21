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

    def __str__(self):
        """
        This class method returns the string representation of
        a square.
        """
        rect_str = "[Square] "
        rect_str += "({}) {}/{} ".format(self.id, self.x, self.y)
        rect_str += "- {}".format(self.width)
        return rect_str
