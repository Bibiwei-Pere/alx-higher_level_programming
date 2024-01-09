#!/usr/bin/python3

"""
This module contains function that prints the name(first and last name)
of the argument supplied to it. The data type of both arguments have to be
 a string and if otherwise, it throws and error.

 """


def say_my_name(first_name, last_name=""):
    """This function prints the name(first and last) supplied
    to it.

    Args:
        first_name: The first string argument
        last_name: The second optional argument

    Raise:
        TypeError: first_name must be a string or last_name must be a string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name.strip(), last_name.strip()))
