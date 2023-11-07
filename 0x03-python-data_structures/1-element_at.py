#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) or idx < 0:
        return None
    for i, val in enumerate(my_list):
        if i == idx:
            return val
