#!/usr/bin/python3
"""
Define a BaseGeometry class
"""


class BaseGeometry:
    """
    Class that defines a BaseGeometry
    """

    def area(self):
        """
        Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value

        Args:
            name: name of the value
            value: value to be validated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
