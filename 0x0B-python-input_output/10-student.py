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
        return vars(self)
    """
    This method  returns the dictionary description of the student object.
    """
    def to_json(self, attrs=None):
        if attrs == None:
            return vars(self)
        all_vars = vars(self)
        filtered = []
        for i in all_vars:
            if i in attrs:
                filtered.append((i, all_vars[i]))
        filtered.reverse()
        return dict(filtered)
    """
    This method retrieves a dictionary representation of a Student
    instance based on attrs filter.
    """
