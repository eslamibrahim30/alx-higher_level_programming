#!/usr/bin/python3
"""
This module for log parsing.
"""
if __name__ == "__main__":
    import sys
    line_c = 0
    line_list = None
    total_size = 0
    msg = ""
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
            total_size += int(line_list[-1])
            s_codes[line_list[-2]] += 1
            line_c += 1
            if line_c == 10:
                msg = ""
                msg += "File size: {}\n".format(total_size)
                for i in s_codes:
                    if s_codes[i] > 0:
                        msg += "{}: {}\n".format(i, s_codes[i])
                print(msg, end="")
                line_c = 0
    except KeyboardInterrupt:
        msg = ""
        msg += "File size: {}\n".format(total_size)
        for i in s_codes:
            if s_codes[i] > 0:
                msg += "{}: {}\n".format(i, s_codes[i])
        print(msg, end="")
        raise
