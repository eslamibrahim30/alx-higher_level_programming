#!/usr/bin/python3
"""
This module for student class.
"""


class Student:
    """
    This class for defining a student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """
    This method for initializing a student object.
    """
    def to_json(self):
        class_to_json = __import__('8-class_to_json').class_to_json
        return class_to_json(self)
    """
    This method  returns the dictionary description of the student object.
    """
