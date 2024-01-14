#!/usr/bin/python3
""" module that defines a class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square definition """

    def __init__(self, size, x=0, y=0, id=None):
        """ class Rectangle object constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get method returns size """
        return self.width

    @size.setter
    def size(self, size):
        """ set method sets private attr, size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args:
            attr = ["id", "size", "x", "y"]
            for key, value in enumerate(args):
                setattr(self, attr[key], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """ returns string repr of Square instance """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        new = {}
        for key, value in vars(self).items():
            if key == "_Rectangle__width":
                new["size"] = value
            elif key == "_Rectangle__height":
                continue
            else:
                new[key.split('_')[-1]] = value
        return new
