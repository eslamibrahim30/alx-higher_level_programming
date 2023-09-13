#!/usr/bin/python3
"""
This module for writing text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file,
    after each line containing a specific string.
    """
    new_text = ""
    with open(filename, 'r') as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, 'w') as f:
        f.write(new_text)
