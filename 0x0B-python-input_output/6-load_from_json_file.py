#!/usr/bin/python3
"""
This module for loading JSON object from a file.
"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)
