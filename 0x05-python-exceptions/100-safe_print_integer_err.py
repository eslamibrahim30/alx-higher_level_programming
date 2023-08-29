#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except TypeError as t:
        print("Exception:", file=sys.stderr, end=" ")
        print(t, file=sys.stderr)
        return False
    except ValueError as v:
        print("Exception:", file=sys.stderr, end=" ")
        print(v, file=sys.stderr)
        return False
    return True
