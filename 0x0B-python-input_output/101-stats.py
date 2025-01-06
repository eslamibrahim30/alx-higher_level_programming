#!/usr/bin/python3
"""
This module for log parsing.
"""
if __name__ == "__main__":
    import sys
    line_c = 0
    l_list = None
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
            l_list = line.split()
            if len(l_list) > 2:
                if l_list[-1].isnumeric():
                    total_size += int(l_list[-1])
                    line_c += 1
                if l_list[-2].isnumeric():
                    s_codes[l_list[-2]] += 1
            if line_c == 10:
                msg = ""
                msg += "File size: {}\n".format(total_size)
                for i in s_codes:
                    if s_codes[i] != 0:
                        msg += "{}: {}\n".format(i, s_codes[i])
                sys.stdout.write(msg)
                line_c = 0
        if line_c > 0 or total_size == 0:
            msg = ""
            msg += "File size: {}\n".format(total_size)
            for i in s_codes:
                if s_codes[i] != 0:
                    msg += "{}: {}\n".format(i, s_codes[i])
            sys.stdout.write(msg)
    except KeyboardInterrupt:
        msg = ""
        msg += "File size: {}\n".format(total_size)
        for i in s_codes:
            if s_codes[i] > 0:
                msg += "{}: {}\n".format(i, s_codes[i])
        sys.stdout.write(msg)
        raise
