#!/usr/bin/python3
def magic_string(counter=[0]):
    counter[0] += 1
    return "{}".format(counter[0] * "BestSchool, ")[:-2]
