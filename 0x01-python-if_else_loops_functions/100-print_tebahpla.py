#!/usr/bin/python3
for i in range(122, 96, -1):
    print(f"{i-((i % 2 != 0)*32):c}", end="")