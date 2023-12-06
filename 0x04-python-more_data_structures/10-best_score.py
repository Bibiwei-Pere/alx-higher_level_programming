#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        maxi = max(list(a_dictionary.values()))
        for i in a_dictionary:
            if a_dictionary[i] == maxi:
                return i
    return None
