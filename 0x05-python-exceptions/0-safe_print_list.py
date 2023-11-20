#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for val in my_list[:x]:
            i += 1
            print(val, end='')
        print("\n")
    except IndexError:
        pass
    return i