#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None
    if not isinstance(roman_string, str):
        return None
    if len(roman_string) == 0:
        return 0
    romans_small = [('I', 1), ('V', 5)]
    romans_mid = [('X', 10), ('L', 50)]
    romans_big = [('C', 100), ('D', 500), ('M', 1000)]
    dict_romans = dict(romans_small + romans_mid + romans_big)
    num = dict_romans[roman_string[-1]]
    for i in range(len(roman_string) - 1):
        if dict_romans[roman_string[i]] < dict_romans[roman_string[i + 1]]:
            num -= dict_romans[roman_string[i]]
        else:
            num += dict_romans[roman_string[i]]
    return num
