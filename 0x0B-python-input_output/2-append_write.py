#!/usr/bin/python3
"""
function that appends a string to a text file (UTF8) and returns the number of
characters added
"""


def append_write(filename="", text=""):
    """
        append_write - append a string to a file and return the number of chars
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
