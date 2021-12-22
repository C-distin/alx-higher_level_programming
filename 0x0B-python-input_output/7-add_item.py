#!/usr/bin/python3
"""
script that add all arguments to a new list, and save the list in a file
"""

# import modules
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f = 'add_item.json'

try:
    load = load_from_json_file(f)
except (ValueError, FileNotFoundError):
    load = []

for i in range(1, len(sys.argv)):
    load.append(sys.argv[i])

save_to_json_file(load, f)
