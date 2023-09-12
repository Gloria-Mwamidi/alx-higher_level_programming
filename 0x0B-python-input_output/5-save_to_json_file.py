#!/usr/bin/python3
"""A function that writs an object to a
textfile using json representation"""

import json


def save_to_json_file(my_obj, filename):
    """"writes an object file to a text file with json"""
    with open(filename, mode="w") as f:
       f.write(json.dumps(my_obj))
