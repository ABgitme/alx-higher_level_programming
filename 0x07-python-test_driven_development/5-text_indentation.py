#!/usr/bin/python3
""" a function that indents a text """


def text_indentation(text):
    """
    Indents a text block according to the following rules:

    * After each of the characters '.', ':', and '?' add two newlines.
    * If the character following one of the
        aforementioned characters is a space, ignore it.

    Args:
        text (str): The text to indent.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str) or (text is None):
        raise TypeError("text must be a string")
    buff = []
    j = 0
    for i, char in enumerate(text):
        if char in ['.', ':', '?']:
            buff.append(char + "\n" + "\n")
        else:
            if text[i - 1] in ['.', ':', '?']:
                j = 1
            if j == 1 and char == ' ':
                continue
            buff.append(char)
            j = 0
    print("".join(buff), end='')
