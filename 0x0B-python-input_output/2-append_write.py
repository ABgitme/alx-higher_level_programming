#!/usr/bin/python3
"""
Module for appending text to files in UTF-8 encoding.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
    - filename (str): The name of the file to
        which the string will be appended.
    - text (str): The string to be appended to the file.

    Returns:
    - int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
