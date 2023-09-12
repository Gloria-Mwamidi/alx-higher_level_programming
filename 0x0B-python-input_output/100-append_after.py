#!/usr/bin/python3
"""Write a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file, after each line """
    string = ""
    with open(filename, mode="r") as read_lines:
        for line in read_lines:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, mode="w") as write_lines:
        write_lines.write(string)
