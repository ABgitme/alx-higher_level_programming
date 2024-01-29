#!/usr/bin/python3
"""
Module for writing text to files in UTF-8 encoding.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.

    Args:
        filename (str, optional): The name of the file
            to write to. Defaults to an empty string.
        text (str, optional): The text to write to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
