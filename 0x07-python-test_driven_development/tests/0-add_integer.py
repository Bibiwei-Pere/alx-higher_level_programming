#!/usr/bin/python3
"""
This module conatins the function for strictly adding 2 numbers
of data type int or floats together, any other data type is regarded
as invalid with exceptions being raise signifying what caused the error.

"""


def add_integer(a, b=98):
    """This function returns the summation of 2 numbers of data type
    int or float together

    Args:
        a: The first number
        b: The second number

    Return: a + b
    """
    data = (int, float)

    if not isinstance(a, data):
        raise TypeError("a must be an integer")
    elif not isinstance(b, data):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
