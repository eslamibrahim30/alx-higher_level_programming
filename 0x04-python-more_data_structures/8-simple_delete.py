#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key is None or not isinstance(a_dictionary, dict):
        return None
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
