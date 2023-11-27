#!/usr/bin/python3
""" A function that prints square using # """


def print_square(size):
    """
    Prints a square of the specified size using the '#' character.

    Args:
        size (int): The size of the square to print.

    Raises:
        TypeError: If `size` is not an integer or a float less than 0.
        ValueError: If `size` is less than 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
