#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastnum = abs(number)
        newnum = lastnum % 10
        print("{:d}".format(newnum), end="")
        return newnum
    else:
        lastnum = number % 10
        print("{:d}".format(lastnum), end="")
        return lastnum
