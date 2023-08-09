#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c_char = ord(i)-(ord(i) >= 97 and ord(i) <= 122)*32;
        print("{:c}".format(c_char), end="")
    print("")
