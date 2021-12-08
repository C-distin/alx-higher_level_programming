#!/usr/bin/python3
"""
Define a Square class
"""


class Square:
    """
    A class that defines a square
    """

    def __init__(self, size=0):
        """
        Initializes the square

        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size of the square

        Args:
            value: size of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

    def __less_than__(self, other):
        """
        Returns True if self is less than other
        """
        return self.__size < other.__size

    def __less_than_or_equal__(self, other):
        """
        Returns True if self is less than or equal to other
        """
        return self.__size <= other.__size

    def __greater_than__(self, other):
        """
        Returns True if self is greater than other
        """
        return self.__size > other.__size

    def __greater_than_or_equal__(self, other):
        """
        Returns True if self is greater than or equal to other
        """
        return self.__size >= other.__size

    def __equal_to__(self, other):
        """
        Returns True if self is equal to other
        """
        return self.__size == other.__size

    def __not_equal_to__(self, other):
        """
        Returns True if self is not equal to other
        """
        return self.__size != other.__size
