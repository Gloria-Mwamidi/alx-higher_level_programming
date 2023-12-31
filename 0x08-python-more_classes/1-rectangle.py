#!/usr/bin/python3

"""Class rectangle that defines width and height"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def heigth(self, value):
        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValuError("height must be >= 0")
        self.__height = value
