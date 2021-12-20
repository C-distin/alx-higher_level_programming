#!/usr/bin/python3
"""
This module contains a function that determines if two classes are the same
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of the specified class

    Args:
        obj: the object to be tested
        a_class: the class to be tested against

    Returns:
        True if the object is an instance or inherited instance
        of the specified class
        False if otherwise
    """
    return isinstance(obj, a_class)
