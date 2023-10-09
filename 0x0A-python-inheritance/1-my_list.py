#!/usr/bin/python3
"""Inheriting class MyList from list"""


class MyList(list):
    """ A subclass for list"""
    def __init__(self):
        """initialization"""
        supper().__init__()

    def print_sorted(self)
    """prints the sorted list"""
    print(sorted(self))
