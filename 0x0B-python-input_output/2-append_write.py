#!/usr/bin/python3
"""Write a function that appends a string at the
end of text file UTF8 and returns the characters added"""


def append_write(filename="", text=""):
    """Appends and returns the characters added"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
