#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    cur_best = 0
    best_key = ''
    for i in a_dictionary:
        if a_dictionary[i] > cur_best:
            best_key = i
            cur_best = a_dictionary[i]
    return best_key
