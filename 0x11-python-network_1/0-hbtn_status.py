#!/usr/bin/python3
"""
This module for task "What's my status? #0"
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
   res = response.read()
   print("Body response:")
   print("\t- type: {}".format(type(res)))
   print("\t- content: {}".format(res))
   print("\t- utf8 content: {}".format(res.decode('utf-8')))
