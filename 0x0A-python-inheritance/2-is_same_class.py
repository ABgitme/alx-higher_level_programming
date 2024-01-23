#!/usr/bin/python3
"""Module for checking object class equality."""


def is_same_class(obj, a_class):
    """
    Checks if an object belongs to a specific class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class,
            False otherwise.
    """
    return type(obj) is a_class
