def magic_string():
    magic_string.i += 1
    return "{}".format(magic_string.i * "BestSchool, ")[:-2]
magic_string.i = 0
