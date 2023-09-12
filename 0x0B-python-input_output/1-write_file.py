#!/usr/bin/python3
"""A function that writes a string to utf8 and
returns the number of strings written, creates it
if not exisitng and overrides existing texts"""


def write_file(filename="", text=""):
    """Writes a string in file UTF8"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
