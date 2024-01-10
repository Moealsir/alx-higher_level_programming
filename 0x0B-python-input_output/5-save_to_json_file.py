#!/usr/bin/python3
"""
whew
"""
import json


def save_to_json_file(my_obj, filename):
    """
    whew
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
