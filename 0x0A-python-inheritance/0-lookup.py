#!/usr/bin/python3
""" A function that returns the List of all available
variables and methods of an object"""


def lookup(obj):
    """Defines a print of available variables"""
    return (dir(obj))
