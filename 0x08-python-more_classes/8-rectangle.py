#!/usr/bin/python3
"""
Define a rectangle class
"""


class Rectangle:
    """
    A class that defines a rectangle

    Attributes:
            number_of_instances: number of instances of the class
            print_symbol: symbol used to print the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle

        Args:
                        width: width of the rectangle
                        height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the square

        Args:
                        value: value to set width to
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
                        value: value to set height to
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height - 1):
            print(self.print_symbol * self.__width)
        return str(str(self.print_symbol) * self.__width)

    def __repr__(self):
        """
        Returns the string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area

        Args:
                        rect_1: first rectangle
                        rect_2: second rectangle

        Raises:
                        TypeError: if rect_1 or rect_2 are not Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
