#!/usr/bin/python3

"""
This module contains a class that create a square by
inheriting the class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class creates a square by inheriting
    class Rectangle

    Attributes:
        __init__(self): Initializes the object
        size: Size of the square
    """
    def __init__(self, size):
        """This initializes the instance with the number of
        arguments in the base class Rectangle

        size: Size of the square
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
