#!/usr/bin/python3
"""
Define a function that adds a new attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """
    Define a function that adds a new attribute to an object if possible
    """
    if setattr(obj, name, value):
        return True
    raise TypeError("can't add new attribute")
