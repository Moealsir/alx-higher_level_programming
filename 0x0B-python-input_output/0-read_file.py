#!/usr/bin/python3
"""
whew
"""


def read_file(filename=""):
    """
    whew
    """
    
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
