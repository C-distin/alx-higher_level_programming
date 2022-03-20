#!/bin/python3
"""
Define a function that finds the peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Function that finds the peak in a list of unsorted integers
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]

    else:
        return None
