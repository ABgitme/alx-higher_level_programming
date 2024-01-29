#!/usr/bin/python3
"""
Module for converting Python objects to JSON strings.
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON string representation of the object.
    """

    return json.dumps(my_obj)
