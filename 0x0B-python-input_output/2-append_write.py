#!/usr/bin/python3
"""
This module for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a') as f:
        written = f.write(text)
        return written
