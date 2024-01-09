#!/usr/bin/python3

"""
This module divides all elements of a matrix whose row
contains int or float data type with an int or float divider
"""


def matrix_divided(matrix, div):
    """This function divides integers in a matrix with an integer
    divider

    Args:
        matrix: A list of lists containing integers
        div: An integer used in dividing the elements of a list

    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Return: A new list containing the result of each division, rounded
    to 2 decimal places
    """
    data = (int, float)
    err = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"

    if div == float("inf"):
        return [[0.0] * len(row) for row in matrix]

    if isinstance(div, data) and div != 0 and isinstance(matrix, list) and \
            len(matrix) != 0:

        length = len(matrix[0])
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError(err)
            else:
                if len(row) != length:
                    raise TypeError(err2)
                elif len(row) == 0:
                    raise TypeError(err)
                else:
                    for i in row:
                        if not isinstance(i, data):
                            raise TypeError(err)
        return [[round(i/div, 2) for i in row] for row in matrix]

    elif not isinstance(div, data):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    elif not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err)
