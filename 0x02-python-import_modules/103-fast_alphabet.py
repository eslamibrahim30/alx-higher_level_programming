#!/usr/bin/python3
a = str(list(map(chr, list(range(65, 91))))).translate({ord(chr(32)): None})
print(a.translate({ord(chr(44)): None, ord(chr(39)): None})[1:-1])
