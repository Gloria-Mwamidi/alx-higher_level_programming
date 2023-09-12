#!/usr/bin/python3
"""A function that reads the textfile UTF8
and prints it out in standard output"""


def read_file(filename=""):
    """Reads and prints in standard out"""
    with open(filename, encoding="utf-8", mode="r") as f:
        print(f.read(), end="")
