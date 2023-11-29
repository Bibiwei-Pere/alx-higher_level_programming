#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            char = ord(char) - 32
        else:
            char = ord(char)
        print("{:c}".format(char), end="")
    print("")
