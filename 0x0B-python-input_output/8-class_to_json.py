#!/usr/bin/python3
"""
Module for converting class instances
to JSON-serializable dictionaries.
"""


def class_to_json(obj):
    """Returns a dictionary representation of an object's
    attributes for JSON serialization.

    Args:
        obj: An instance of a class with serializable
        attributes (lists, dicts, strings, ints, bools).

    Returns:
        dict: A dictionary containing the object's
        attributes and their values.
    """

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result
