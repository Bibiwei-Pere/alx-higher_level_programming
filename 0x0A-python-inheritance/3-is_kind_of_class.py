#!/usr/bin/python3

"""
This module contains function that checks if the object
pased is an instance of or if is an instance of a class
that inherited from specified class
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is exactly an instance of or instance of an
    instance of a class inherited from the specified class
    class

    Args:
        obj: The object to check
        a_class: The specified class

    Return:
        True: If obj is an instance
        False: If otherwise
    """
    return isinstance(obj, a_class)
