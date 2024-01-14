#!/usr/bin/python3
""" module that defines a class Base """
from json import dumps, loads
import csv


class Base:
    """ class Base definition """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class Base object Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string repr of list_dictionaries """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string repr of list_objs to a file """
        if list_objs is not None:
            list_objs = [objs.to_dictionary() for objs in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string repr json_string """
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a file """
        from os import path
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, "r",  encoding="utf-8") as f:
            return [cls.create(**o) for o in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serilizes object to csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open("{}.csv".format(cls.__name__), "w", newline="",
                  encoding="utf-8") as f:
            wr = csv.writer(f)
            wr.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """ deserilizes object frm csv file """
        from models.rectangle import Rectangle
        from models.square import Square
        list_objs = []
        with open("{}.csv".format(cls.__name__), "r", newline="",
                  encoding="utf-8") as f:
            rd = csv.reader(f)
            for row in rd:
                row = [int(objs) for objs in row]
                if cls is Rectangle:
                    objs = {"id": row[0], "width": row[1], "height": row[2],
                            "x": row[3], "y": row[4]}
                else:
                    objs = {"id": row[0], "size": row[1], "x": row[2],
                            "y": row[3]}
                list_objs.append(cls.create(**objs))
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' turtle graphics draws all the Rectangles and Squares '''
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for item in list_rectangles + list_squares:
            img = turtle.Turtle()
            img.color((randrange(255), randrange(255), randrange(255)))
            img.pensize(1)
            img.penup()
            img.pendown()
            img.setpos((item.x + img.pos()[0], item.y - img.pos()[1]))
            img.pensize(10)
            for i in range(2):
                img.forward(item.width)
                img.left(90)
                img.forward(item.height)
                img.left(90)
            img.end_fill()
        time.sleep(5)
