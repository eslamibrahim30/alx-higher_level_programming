#!/usr/bin/python3
"""
This module for saving JSON object to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file,
    using a JSON representation.
    """
    with open(filename, 'w') as f:
        written = f.write(json.dumps(my_obj))
