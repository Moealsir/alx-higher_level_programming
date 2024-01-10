#!/usr/bin/python3
"""
whew
"""
import json


def load_from_json_file(filename):
    """
    whew
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
