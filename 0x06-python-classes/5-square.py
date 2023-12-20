#!/usr/bin/python3
"""
    Module 5-square
    It defines a square by private instance attribute

"""


class Square:
    """This defines a square by private attribute

        Attributes:
            size: The size of the square

        Methods:
            __init__(self, size=0)
            area(self)
            my_print(self)

    """

    def __init__(self, size=0):
        """This initializes the instance / object with optional
        size (integer)

        Args:
            size: The size of the square

        """
        self.size = size

    @property
    def size(self):
        """
        getter method

        Returns:
            size

        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """
        setter method

        Args:
            new_size: The new size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0 i.e negavive

        """
        if type(new_size) != int:
            raise TypeError("size must be an integer")

        elif new_size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = new_size

    def area(self):
        """Computes the area of the square by raising size to power of 2

        Returns:
            The area of the square

         """
        return self.__size**2

    def my_print(self):
        """Print to stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
