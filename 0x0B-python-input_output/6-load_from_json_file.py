#!/usr/bin/python3
"""Creates an object file from an json file"""
import json


def load_from_json_file(filename):
    """creates object from json file"""
    with open(filename, mode="r") as f:
        json.loads(f)
