#!/usr/bin/python3
"""Defining a class square and computing area
of a square inherited from the class
Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class square inherited from Rectangle"""
    def __init__(self, size):
        """Initialization of the class square"""
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        """returns the area"""
        return self._size ** 2
