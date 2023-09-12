#!/usr/bin/python3
"""
This module for reading a file.
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.read()
        print(lines, end="")
