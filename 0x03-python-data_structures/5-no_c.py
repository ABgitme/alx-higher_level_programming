#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i, ch in enumerate(my_string):
        if ch in ('c', 'C'):
            continue
        else:
            new_string += ch
    return new_string
