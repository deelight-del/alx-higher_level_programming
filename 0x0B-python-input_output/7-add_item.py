#!/usr/bin/python3
"""This module contains the script of the function to save given/
parsed arguments to the scripts as a list object to a json file.
"""
import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

listOfArgs = []

if (len(sys.argv) == 1):
    pass
else:
    for args in sys.argv[1:]:
        listOfArgs.append(args)
path = Path('add_item.json')

if path.exists():
    former_list = load_from_json_file(path)
    former_list.extend(listOfArgs)
    save_to_json_file(former_list, path)
else:
    save_to_json_file(listOfArgs, path)
