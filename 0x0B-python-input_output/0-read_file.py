#!/usr/bin/python3
"""
Module for reading the contents of files.

This module provides the read_file() function, which allows you to read
the entire content of a specified file and print it to the console.
"""


def read_file(filename=""):
    """
    Reads the content of a file and prints it to the console.

    Args:
        filename (str, optional): The name or path of the file to read.
            Defaults to an empty string, indicating the current script.

    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
