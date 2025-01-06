#!/usr/bin/python3
"""
This module for log parsing.
"""
if __name__ == "__main__":
    import sys
    import re
    line_c = 0
    line_list = None
    p = re.compile('\d+\.\d+\.\d+\.\d+ \- \[\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+\] "[a-zA-Z]+ \S+ \S+" \d+ \d+', re.IGNORECASE)
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
            if not p.match(line):
                continue
            line_list = line.split()
            total_size += int(line_list[-1])
            s_codes[line_list[-2]] += 1
            line_c += 1
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
