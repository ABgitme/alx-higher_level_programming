#!/usr/bin/python3
"""
Module for saving objects to text files using JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a text file using JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file to save the object to.
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)  # Serialize object to JSON and write to file
