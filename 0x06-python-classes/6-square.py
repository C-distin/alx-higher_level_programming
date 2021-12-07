#!/usr/bin/python3
"""
Define a Square class
"""


class Square:
    """
    A class that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square

        Args:
                size: size of the square
                postion: position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
                value: size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
                value: position of the square
        """
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int \
                or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
