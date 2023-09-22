#!/usr/bin/python3
"""
This module contains the Base class.
"""
import json
import os
import csv


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
        rs = None
        if cls.__name__ == "Rectangle":
            rs = cls(2, 3)
        else:
            rs = cls(2)
        rs.update(**dictionary)
        return rs

    @classmethod
    def load_from_file(cls):
        """
        This class method returns a list of instances.
        """
        text = ""
        file_name = "{}.json".format(cls.__name__)
        if not os.path.isfile(file_name):
            return []
        with open(file_name, "r") as f:
            text = f.read()
        json_list = Base.from_json_string(text)
        list_inst = []
        for inst in json_list:
            new_inst = cls.create(**inst)
            list_inst.append(new_inst)
        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This class method writes the CSV string representation of
        list_objs to a file.
        """
        file_name = "{}.csv".format(cls.__name__)
        if list_objs is None or len(list_objs) == 0:
            with open(file_name, "w", newline='') as f:
                pass
        else:
            if cls.__name__ == "Rectangle":
                with open(file_name, "w") as f:
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for obj in list_objs:
                        writer.writerow(obj.to_dictionary())

            else:
                with open(file_name, "w") as f:
                    fieldnames = ['id', 'size', 'x', 'y']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for obj in list_objs:
                        writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        This class method returns a list of instances.
        """
        file_name = "{}.csv".format(cls.__name__)
        if not os.path.isfile(file_name):
            return []
        rs_list = []
        with open(file_name, "w") as f:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rs.append(cls(row))
        return rs_list
