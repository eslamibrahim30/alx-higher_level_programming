#!/usr/bin/python3
"""
This module contains only one function
which is used for text indentation
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    end_or_start = 1
    for c in text:
        if end_or_start == 1 and c == ' ':
            pass
        elif c in ['.', '?', ':']:
            print(c)
            print("")
            end_or_start = 1
        else:
            print(c, end="")
            end_or_start = 0
