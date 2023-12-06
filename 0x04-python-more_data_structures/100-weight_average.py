#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    product, avg = 0, 0

    for i in my_list:
        calc = i[0] * i[1]
        product += calc
        avg += i[1]
    return product / avg
