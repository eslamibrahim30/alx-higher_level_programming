#!/usr/bin/python3
def no_c(my_string):
    list_chars = []
    for i in my_string:
        if i != 'c' and i != 'C':
            list_chars.append(i)
    new_string = ''
    for i in list_chars:
        new_string += i
    return new_string
