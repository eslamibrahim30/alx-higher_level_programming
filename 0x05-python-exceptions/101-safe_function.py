#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = None
    try:
        result = fct(*args)
    except ValueError as v:
        print("Exception:", file=sys.stderr, end=" ")
        print(v, file=sys.stderr)
        return None
    except TypeError as t:
        print("Exception:", file=sys.stderr, end=" ")
        print(t, file=sys.stderr)
        return None
    except ZeroDivisionError as z:
        print("Exception:", file=sys.stderr, end=" ")
        print(z, file=sys.stderr)
        return None
    except IndexError as i:
        print("Exception:", file=sys.stderr, end=" ")
        print(i, file=sys.stderr)
        return None
    return result
