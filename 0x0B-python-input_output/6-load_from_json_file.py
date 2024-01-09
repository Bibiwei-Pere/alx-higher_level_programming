#!/usr/bin/python3

"""
This module contains function that creates an object from a JSON file
"""


def load_from_json_file(filename):
    """Creates an object from JSON file

    Args:
        filename: The json file to create object from

    """
    import json

    with open(filename, encoding="utf-8") as f:
        my_obj = json.loads(f.read())
    return my_obj
