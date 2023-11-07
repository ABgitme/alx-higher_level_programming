#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i, val in enumerate(my_list):
        nw_list = list(my_list)
        if idx < 0:
            return nw_list
        elif idx > len(my_list) - 1:
            return nw_list
        else:
            if idx == i:
                nw_list[idx] = element
                return nw_list
