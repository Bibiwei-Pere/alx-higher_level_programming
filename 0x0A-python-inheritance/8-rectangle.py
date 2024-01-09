#!/usr/bin/python3

"""
This module contains a class that inherit base geometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This creates a rectangle, being an inheritance
    of BaseGeometry class

    Attributes:
        __init__(self) - Initializes the object
        width - The width of the rectangle
        height - The height of the rectangle
    """
    def __init__(self, width, height):
        """Initializes the instance"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
