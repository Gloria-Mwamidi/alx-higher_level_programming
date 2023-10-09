#!/usr/bin/python3
"""A function that Defines a class square
inherited from rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """initialization of the class square"""
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def __str__(self):
        """prints out string ducumentation"""
        return "[Square] {}/{}".format(self._size, self._size)

    def area(self):
        """computes the areas of a square"""
        return self._size ** 2
