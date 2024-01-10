#!/usr/bin/python3
"""
whew
"""


def class_to_json(obj):
    """
    whew
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
