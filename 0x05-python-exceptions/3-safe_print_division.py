#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        total = int(a) / int(b)
    except (ZeroDivisionError, TypeError):
        total = None
    finally:
        print("Inside result: {}".format(total))
    return total
