#!/usr/bin/python3
from args import get_args
if __name__ == "__main__":
    arg = []
    arg = get_args()
    length = len(arg)
    if length == 0:
        print("0 arguments.")
    else:
        if length > 2:
            print("{} arguments:".format(length - 1))
        else:
            print("{} argument:".format(length - 1))
        for i in range(length):
            if i != 0:
                print("{}: {}".format(i, arg[i]))
