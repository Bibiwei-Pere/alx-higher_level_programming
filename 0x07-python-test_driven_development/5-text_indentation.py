#!/usr/bin/python3

"""
This module contains function that adds identation to text by
printing a text with 2 new linex after each of these characters
".", "?" and ":"

"""


def text_indentation(text):
    """This function accepts a string and prints a text with
    2 new lines after each of these characters ".", "?" and ":"

    Args:
        text: The string to be supplied

    Raise:
        TypeError: text must be a string

    """
    delim = (".", "?", ":")

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        new = ""
        for i in text:
            new += i
            if i in delim:
                print(new.strip(), end="\n\n")
                new = ""
        print(new.strip(), end="")
