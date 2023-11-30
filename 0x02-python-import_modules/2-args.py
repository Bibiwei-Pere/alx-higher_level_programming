#!/usr/bin/python3
import sys

def args():
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
if __name__ == '__main__':
    args()
