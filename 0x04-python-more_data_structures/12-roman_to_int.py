#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_romans = dict([('I', 1), ('V', 5), ('X', 10),
        ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
    num = dict_romans[roman_string[-1]]
    for i in range(len(roman_string) - 1):
        if dict_romans[roman_string[i]] < dict_romans[roman_string[i + 1]]:
            num -= dict_romans[roman_string[i]]
        else:
            num += dict_romans[roman_string[i]]
    return num
