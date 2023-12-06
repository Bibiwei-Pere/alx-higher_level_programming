#!/usr/bin/python3


def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0
    result = 0
    zip_str = zip(roman_string, roman_string[1:])

    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i, j in zip_str:
        if i not in dic.keys():
            return 0
        elif dic[i] >= dic[j]:
            result += dic[i]
        else:
            result -= dic[i]
    result += dic[roman_string[-1]]
    return (result)
