#!/usr/bin/python3
"""A function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:

Prototype: def class_to_json(obj):
obj is an instance of a Class
All attributes of the obj Class are serializable: list,
dictionary, string, integer and boolean"""


def class_to_json(obj):
    """define class to json"""
    return obj.__dict__
