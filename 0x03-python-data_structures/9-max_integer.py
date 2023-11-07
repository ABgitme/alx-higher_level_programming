#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]
    for element in my_list:
        if element > max_value:
            max_value = element
    return max_value
