#!/usr/bin/python3

"""
    A Function that returns a list of lists of Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Creates an object from a JSON file.

    Args:
        n (int): The number of lists to create.

    Returns:
        list of lists of Pascal’s triangle of n.
        [1]
        [1,1]
        [1,2,1]
        [1,3,3,1]
        [1,4,6,4,1]
    """

    triangle = []
    row = []
    for i in range(n):
        if i == 0:
            row[i] = 1
        for j in range(1, i + 1):
            if j == 0:
                row[j]
        
        

    return triangle
