#!/usr/bin/python3
"""
This module contains a function that determines if one class is inherited
directly or indirectly from another class
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of the specified class
    or inherited from it

    Args:
        obj: the object to be tested
        a_class: the class to be tested against

    Returns:
        True if the object is an instance of the specified class
        or inherited from it
        False if otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
