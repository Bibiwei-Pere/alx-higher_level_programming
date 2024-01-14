#!/usr/bin/python3
""" module that defines a class Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ class Rectangle definition """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class Rectangle object constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get method returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set method sets private attr, width """
        self.validate_value("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ get method returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set method sets private attr, height """
        self.validate_value("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ get method returns x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set method sets private attr, x """
        self.validate_value("x", value)
        self.__x = value

    @property
    def y(self):
        """ get method returns y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set method sets private, y """
        self.validate_value("y", value)
        self.__y = value

    def validate_value(self, name, value, flag=True):
        """  validates attribute value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if flag and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not flag and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ returns the area value of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle with # """
        draw = '\n' * self.y + \
               (' ' * self.x + '#' * self.width + '\n') * self.height
        print(draw, end='')

    def __str__(self):
        """ returns string repr of rectangle instance """
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """updates instance attribtes via *args/**kwargs variables"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
