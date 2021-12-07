#!/usr/bin/python3
class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
                size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
                value (int): The size of the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
