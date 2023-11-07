#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i, val in enumerate(my_list[::-1]):
        print('{}'.format(val))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)