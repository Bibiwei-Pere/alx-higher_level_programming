#!/usr/bin/python3

"""
This module contains a class that creates a base geometry
"""


class BaseGeometry:
    """This creates a base geometry class

    Attributes:
        area(self) - The area of the base geometry
        integer_validator(self, name, value) - Validates values
        __init__(self) - Initializes the object
        name - Name of geometry
        value - Value of geometry

    Raise:
        Exception
    """
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates values

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
