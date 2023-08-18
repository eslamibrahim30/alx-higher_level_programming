#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not isinstance(a_dictionary, dict):
        return None
    new_dict = []
    for key in a_dictionary.keys():
        if a_dictionary[key] != value:
            new_dict.append((key, a_dictionary[key]))
    a_dictionary.clear()
    a_dictionary.update(dict(new_dict))
    return a_dictionary
