#!/usr/bin/python3
"""
Module for loading objects from JSON files.
import json
"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        The Python object represented by the JSON data in the file.
    """

    with open(filename, "r") as f:
        return json.load(f)  # Load JSON data from file and return the object
