#!/usr/bin/python3
"""A function that Defines a class rectangle that
inherites from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherited"""

    def __init__(self, width, height):
        """Initialization of class Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
