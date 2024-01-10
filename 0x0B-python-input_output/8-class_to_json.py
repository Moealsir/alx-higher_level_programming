#!/usr/bin/python3
"""
whew
"""

def class_to_json(obj):
    """
    whew
    """
    
    res = {}
    if hasattr(obj, "__dist__"):
        res = obj.__dist__.copy()
        return res
