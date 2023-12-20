#!/usr/bin/python3
"""
    Module 5-square
    It defines a square by private instance attribute

"""


class Square:
    """This defines a square by private attribute

        Attributes:
            size: The size of the square
            position: Tuple of 2 positive integers

        Methods:
            __init__(self, size=0)
            area(self)
            my_print(self)

    """

    def __init__(self, size=0, position=(0, 0)):
        """This initializes the instance / object with optional
        size (integer)

        Args:
            size: The size of the square
            position: Tuple of 2 positive integers

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter method

        Returns:
            size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method

        Args:
            value: The new value for square size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0 i.e negavive

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        getter method

        Return:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter method

        Args:
            value: The new position turple

        Raises:
            TypeError: If the turple is not of 2 integers

        """
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(i, int) for i in value)
                or not all(j >= 0 for j in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Computes the area of the square by raising size to power of 2

        Returns:
            The area of the square

         """
        return (self.__size)**2

    def my_print(self):
        """Print to stdout the square with character # and with spaces"""

        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
