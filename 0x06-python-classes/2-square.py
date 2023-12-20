#!/usr/bin/python3
"""
	Module 2-square
	Square class now has an if statement
"""


class Square:
    """This defines a private Square attribute"""
    def __init__(self, size=0):
        """If statement"""
        if type(size) != int:
            """Raise an error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """Raise an error"""
            raise ValueError("size must be >= 0")
        else:
            """initialize __size of self with size"""
            self.__size = size
