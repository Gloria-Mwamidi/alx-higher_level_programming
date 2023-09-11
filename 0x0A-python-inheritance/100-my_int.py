#!/usr/bin/python3
"""A class MyIntt that inherits from int"""


class MyInt(Int):
    """Class MyInt inherited from Int"""
    def __eq__(self, other):
        """Magic inheritance of the equal sign"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Magic inheritance of the not equal sign"""
        return not super().__ne__(other)
