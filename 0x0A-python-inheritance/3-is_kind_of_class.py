#!/usr/bin/python3
"""Defines a function that return true if
the object is an instance of inherited
class otherwise returns a false"""


def is_kind_of_class(obj, a_class):
    """Check the inheritance using isinstance"""
    return isinstance(obj, a_class)
