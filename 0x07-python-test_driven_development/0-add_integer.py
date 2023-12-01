#!/usr/bin/python3
""" This function is used to add two numbers."""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a (int | float): The first integer or float to add.
        b (int | float, optional): The second integer
            or float to add. Defaults to 98.

    Raises:
        TypeError: If either `a` or `b` is not an integer, float, or string.

    Returns:
        int: The sum of `a` and `b`.
    """
    if not (isinstance(a, int) or isinstance(a, float)) or isinstance(a, str):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)) or isinstance(b, str):
        raise TypeError("b must be an integer")
    if a == float('inf') or b == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if a == -float('inf') or b == -float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if a == float('nan') or b == float('nan'):
        raise ValueError("cannot convert float nan to integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
