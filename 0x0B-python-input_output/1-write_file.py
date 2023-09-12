#!/usr/bin/python3
"""
This module for writing text to a file.
"""

def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8)
    and returns the number of characters written.
    """
    with open(filename, 'w') as f:
        written = f.write(text)
        return written
