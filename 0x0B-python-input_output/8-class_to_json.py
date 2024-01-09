#!/usr/bin/python3

"""
This module contains function that returns dictionary description
with simple data structuree.g list, dictionary, string, integer
and boolean, for JSON serialization of an object.
"""


def class_to_json(obj):
    """Return the dictionary description for simple
    data structure e.g list, dictionary, string, integer
    and booloean, for JSON serialization
    """

    return obj.__dict__
