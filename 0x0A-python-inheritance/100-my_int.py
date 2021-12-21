#!/usr/bin.python3
"""
Define a class MyInt that inherits from int
"""


class MyInt(int):
    """
    Class MyInt that inherits from int
    """

    def __eq__(self, other):
        """
        Override the == operator
        """
        if int.__eq__(self, other) is True:
            return False
        return True

    def __ne__(self, other):
        """
        Override the != operator
        """
        if int.__ne__(self, other) is True:
            return False
        return True
