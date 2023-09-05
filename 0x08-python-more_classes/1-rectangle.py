#!/usr/bin/python3

"""Class rectangle that defines width and height"""


class rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def heigth(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def heigth(self, value):
        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValuError("height must be >= 0")
        self.__height = value
