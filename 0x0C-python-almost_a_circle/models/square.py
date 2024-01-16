#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square:
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)
