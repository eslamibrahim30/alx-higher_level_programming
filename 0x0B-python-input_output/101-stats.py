#!/usr/bin/python3
"""
This module for log parsing.
"""
import sys
from time import sleep
line = ""
line_c = 0
line_list = None
total_size = 0
s_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
try:
    for line in sys.stdin:
        line_list = line.split()
        if line_c == 10:
            print("File size: {}".format(total_size))
            for i in s_codes:
                if s_codes[i] > 0:
                    print("{}: {}".format(i, s_codes[i]))
            line_c = 0
        else:
            total_size += int(line_list[-1])
            s_codes[line_list[-2]] += 1
            line_c += 1
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for i in s_codes:
        if s_codes[i] > 0:
            print("{}: {}".format(i, s_codes[i]))
