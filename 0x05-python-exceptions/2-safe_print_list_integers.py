#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    for i in range(x):
        try:
            val = my_list[i]
            print("{:d}".format(val), end='')
            printed_count += 1
        except (ValueError, TypeError):
            continue
    print()
    return printed_count
