#!/usr/bin/python3
"""
This module contains MyList class that inherits from list.
"""


class MyList(list):
    """
    This class is a custom written list class.
    """
    def print_sorted(self):
        print(sorted(self))
    """
    This method prints the list, but sorted (ascending sort)
    """
