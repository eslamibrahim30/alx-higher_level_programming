#!/usr/bin/python3
"""
This module for task "What's my status? #0"
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except urllib.error.URLError as e:
        print('Error code: {}'.format(e.code))
