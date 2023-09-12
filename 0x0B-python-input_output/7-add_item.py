#!/usr/bin/python3
"""Writes a script that adds all arguments to a Python
list, and then saves them to a file:
use your function save_to_json_file from 5-save_to_json_file.py
use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation
in a file named add_item.json"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
loads_from_json_file = __import__('6-loads_from_json_file')
.loads_from_json_file

try:
    info = loads_from_jason_file("add_item.json")
except FileNotFoundError:
    info = []

for i in range(1, len(sys.agrv)):
    info.append(sys.agrv[i])
    save_to_json_file(info, "add_item.json")
