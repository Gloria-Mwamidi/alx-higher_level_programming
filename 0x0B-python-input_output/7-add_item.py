#!/usr/bin/python3
"""
Writes a script that adds all arguments to a Python list
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
loads_from_json_file = __import__('6-loads_from_json_file').loads_from_json_file

try:
    info = loads_from_json_file("add_item.json")
except FileNotFoundError:
    info = []

for i in range(1, len(sys.agrv)):
    info.append(sys.agrv[i])
    save_to_json_file(info, "add_item.json")
