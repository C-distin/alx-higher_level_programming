#!/usr/bin/python3
"""
contains class Square which implements Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square which implements rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the instance of the class

        Args:
            size: size of the square
            x: x coordinate of the square
            y: y coordinate of the square
            id: id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns string representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)
