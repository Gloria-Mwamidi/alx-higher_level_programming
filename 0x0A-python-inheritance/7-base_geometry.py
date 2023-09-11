#!/usr/bin/python3
""" Defines class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """function not done"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the type and value of the vaiable
        value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
