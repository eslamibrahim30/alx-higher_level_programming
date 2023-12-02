#!/usr/bin/python3
"""
This module for task "Response header value #0"
"""
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    res = response.info()
    print(res['X-Request-Id'])
