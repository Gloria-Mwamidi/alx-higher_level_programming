#!/usr/bin/python3
"""A function of class Rectangle that inherites from
BaseGeometry and the area() implemented"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inheritaed"""

    def __init__(self, width, height):
        """Initialization of class Rectangle"""
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height

    def __str__(self):
        """returns th rectangles descreption"""
        return "[Rectangle]{}/{}".format(self._width, self._height)

    def area(self):
        """computes the area of a rectangle"""
        return self._width * self._height
