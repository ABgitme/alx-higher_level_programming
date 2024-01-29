#!/usr/bin/python3
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename
filename = "add_item.json"

# Check if the file exists
if not path.exists(filename):
    # Create an empty list if the file doesn't exist
    items_list = []
else:
    # Load the existing list from the file
    items_list = load_from_json_file(filename)

# Add the arguments to the list
for arg in sys.argv[1:]:
    items_list.append(arg)

# Save the updated list to the file
save_to_json_file(items_list, filename)