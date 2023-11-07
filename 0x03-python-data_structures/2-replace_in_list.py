#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i, val in enumerate(my_list):
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
        else:
            if idx == i:
                my_list[idx] = element
                return my_list
