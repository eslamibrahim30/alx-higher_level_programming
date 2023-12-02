#!/usr/bin/python3
"""
This module for task "Response header value #1"
"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
