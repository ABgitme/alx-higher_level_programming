#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    for element in my_list:
        if my_list == '':
            return 'None'
        elif element > max_value:
            max_value = element
    return max_value
