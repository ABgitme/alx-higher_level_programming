#!/usr/bin/python3
"""
Module for converting JSON strings to Python objects.
"""


import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: The JSON string to be parsed into a Python object.

    Returns:
        The Python object represented by the JSON string.
    """

    return json.loads(my_str)
