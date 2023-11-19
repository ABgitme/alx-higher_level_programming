#!/usr/bin/python3
import sys
def infadd():
    arg_list = []
    arg_list = sys.argv
    length = len(arg_list)
    if length == 1:
        return 0
    else:
        my_list = list()
        for i in range(length):
            if i != 0:
                my_list.append(int(arg_list[i]))
        return sum(my_list)
