#!/usr/bin/python3
"""A function that returns an json representation to
a string"""
import json


def from_json_string(my_str):
    """Returns json representation to an object string"""
    return json.loads(my_str)
