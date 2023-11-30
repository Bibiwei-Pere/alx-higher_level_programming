#!/usr/bin/python3
import sys


def infinite_add():
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print("{}".format(sum))
if __name__ == '__main__':
    infinite_add()
