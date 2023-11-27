#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str) or text is None:
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
    print("".join(buff))
