#!/usr/bin/python3
"""Function  that defines A class MyInt that inherits from int"""


class MyInt(int):
    """Class MyInt inherited from Int"""
    def __eq__(self, other):
        """Magic inheritance of the equal sign"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Magic inheritance of the not equal sign"""
        return not super().__ne__(other)
