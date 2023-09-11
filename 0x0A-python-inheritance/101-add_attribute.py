#!/usr/bin/python3
"""Defines a function that adds a new attribute"""


def add_attribute(obj, att, value):
    """adds the attributes"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
