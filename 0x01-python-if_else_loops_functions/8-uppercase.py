#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print(f"{ord(i)-32:c}", end="")
        else:
            print(f"{i}", end="")
    print("")