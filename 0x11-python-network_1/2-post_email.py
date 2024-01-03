#!/usr/bin/python3
"""
This module for task "POST an email #0"
"""
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
