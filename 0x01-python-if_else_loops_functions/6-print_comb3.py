#!/usr/bin/python3
for digit in range(0, 10):
    for digits in range((digit + 1), 10):
        if (digit != 8) or (digits != 9):
            print("{}{}, ".format(digit, digits), end="")
        else:
            print("{}{}, ".format(digit, digits))
