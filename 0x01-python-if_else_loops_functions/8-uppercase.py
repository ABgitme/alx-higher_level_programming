#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i, char in enumerate(str):
        if (ord(char) not in range(65, 91)) and (ord(char) in range(97, 123)):
            print("{}".format(chr(ord(char) - 32)), end='' if (i < length - 1) else "\n")
        else:
            print("{}".format(str[i]), end='' if (i < length - 1) else "\n")
