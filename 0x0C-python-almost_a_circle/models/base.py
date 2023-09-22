#!/usr/bin/python3
"""
This module contains the Base class.
"""
import json


class Base:
    """
    This class will be the 'base' of all other classes in this project.
    The goal of it is to manage id attribute in all future classes and
    to avoid duplicating the same code (by extension, same bugs).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method initializes a new created Base object.
        """
        if id is not None:
            Base.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Thi class method returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This class method writes the JSON string representation of
        list_objs to a file.
        """
        file_name = "{}.json".format(cls.__name__)
        if list_objs is None or len(list_objs) == 0:
            with open(file_name, "w") as f:
                text = Base.to_json_string([])
                f.write(text)
        else:
            new_list = []
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            with open(file_name, "w") as f:
                text = Base.to_json_string(new_list)
                f.write(text)

    @staticmethod
    def from_json_string(json_string):
        """
        This static method returns the list of the JSON string
        representation json_string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This class method returns an instance with all attributes already set.
        """
        rs = cls(2, 3)
        rs.update(dictionary)
        return rs
