#!/usr/bin/python3
def magic_string():
    class MagicString:
        def __init__(self):
            self.str = ""
        def __str__(self):
            if self.str == "":
                self.str = "BestSchool"
            else:
                self.str += ", BestSchool"
            return self.str
