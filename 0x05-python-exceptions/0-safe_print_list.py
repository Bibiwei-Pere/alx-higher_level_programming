#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    len = 0
    while len < x:
        try:
            print("{}".format(my_list[len]), end="")
        except IndexError:
            break
        len += 1
    print("")
    return len
