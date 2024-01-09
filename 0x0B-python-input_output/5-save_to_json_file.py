#!/usr/bin/python3

"""
This module contains function that writes an object to a text file,
using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation

    Args:
        my_obj: The object to write to text file
        filename: The file to write the object to
    """
    import json

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
