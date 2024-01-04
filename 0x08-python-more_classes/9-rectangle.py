#!/usr/bin/python3

"""
This module contains a class that defines a Rectangle with
private attribute width

"""


class Rectangle:
    """This class defines a rectangle

    Attributes:
        number_of_instances: Counter for number of instances created
        or deleted
        print_symbol: Used as symbol for string representation
        width: The width of rectangle
        height: The height of rectangle
        __init__(self, width=0, height=0)
        area: The rectangle area
        perimeter: The rectangle perimeter
        __str__: Print the rectangle
        __repr__: Return string representation of the rectangle
        __del__: Print delete message
        bigger_or_equal(rect_1, rect_2)
        square(cls, size=0)

    Raise:
        TypeError: width must be an integer
        ValueError: width must be >= 0
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This method initializes the class instance

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """This method retrieves the width of the rectangle

        Return: The width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This method set the new value of the width

        Args:
            value: The new width
        Raise:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """This method retrieves the height of the rectangle

        Return: The height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """This method set the new value of the height

        Args:
            value: The new height
        Raise:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """This returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """This prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        display = '\n'.join([str(self.print_symbol) * self.__width
                            for i in range(self.__height)])
        return display

    def __repr__(self):
        """Return string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Print delete message"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This compares 2 instances based on their area

        Args:
            rect_1: The first instance of Rectangle
            rect_2: The second instance of Rectangle

        Raises:
            TypeError: if either rect_1 or rec_2  is not an
            instance of Rectangle

        Return:
            rect_1: if first instance area >= second instance area
            rect_2: if first instance area < second instance area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return rect_1 if rect_1.area() >= rect_2.area()\
                    else rect_2

    @classmethod
    def square(cls, size=0):
        """This returns a new Rectangle instance with
        width == height == size

        Args:
            size: The new Rectangle instance size

        Return: New instance of Rectangle
        """
        return cls(size, size)
