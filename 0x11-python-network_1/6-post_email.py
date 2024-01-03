#!/usr/bin/python3
"""
This module for task "POST an email #1"
"""
if __name__ == "__main__":
    import requests
    import sys
    values = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=values)
    print(r.text)
