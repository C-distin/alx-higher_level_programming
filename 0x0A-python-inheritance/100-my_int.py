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
        return self.__int__() != other

    def __ne__(self, other):
        """
        Override the != operator
        """
        return self.__int__() == other
