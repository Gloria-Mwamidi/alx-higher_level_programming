#!/usr/bin/python3
"""Defines a fuction that returns true idf the object is an
instance of a class inherited directly or
indirectly otherwise returns false"""


def inherits_from(obj, a_class):
    """checks if the obj is an instance of the class"""
    if obj.__class == a_class:
        return false
    return isinstance(obj, a_class) or issubclass(obj.__class__, a_class)
