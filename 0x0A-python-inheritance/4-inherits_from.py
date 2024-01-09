#!/usr/bin/python3

"""
This module contains function that checks if the object
pased is a subclass of a base class i.e checks inheritance
"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of a class that inherit the
    specified class

    Args:
        obj: The object to check
        a_class: The specified class

    Return:
        True: If obj is an inheritance of a_class and it's type is not
        a_class
        False: If otherwise
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
