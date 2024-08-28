#!/usr/bin/python3
"""
File Manipulation Module

This module provides functionality
to manipulate text files, specifically
to insert a new line of text after each
line containing a specified string.

Functions:
    append_after(filename, search_string, new_string):
    Inserts a line of text
    after each line containing
    a specific string in the given file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text into a file
    after each line containing a specific string.

    Args:
        filename (str): The path to the file to be modified.
        search_string (str): The string to search for
        in each line of the file.
        new_string (str): The string to insert after each line
        that contains the search_string.
    """
    # Open the file for reading and writing
    with open(filename, "r") as file:
        lines = file.readlines()  # Read all lines into a list

    # Open the file for writing
    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)  # Append the new string after the line
