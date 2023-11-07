#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_len = len(tuple_a)
    tuple_b_len = len(tuple_b)
    new_tuple = list()
    if tuple_a_len < 2:
        for i in range(2 - tuple_a_len):
            tuple_a += (0,)
    if tuple_b_len < 2:
        for i in range(2 - tuple_b_len):
            tuple_b += (0,)
    if tuple_a_len > 2:
        tuple_a = tuple_a[:2]
    if tuple_b_len > 2:
        tuple_b = tuple_b[:2]
    new_tuple.append(tuple_a[0] + tuple_b[0])
    new_tuple.append(tuple_a[1] + tuple_b[1])
    return new_tuple
