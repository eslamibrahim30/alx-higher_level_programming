#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    sorted_keys = sorted(a_dictionary)
    for key in sorted_keys:
        print('{}: {}'.format(key, a_dictionary[key]))
