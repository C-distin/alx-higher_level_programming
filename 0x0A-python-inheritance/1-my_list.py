#!/usr/bin/python3
"""
Define a Class MyList that inherits from list
"""


class MyList(list):
    """
    Define a Class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Print the list, but sorted (ascending sort)
        """
        print(sorted(self))
