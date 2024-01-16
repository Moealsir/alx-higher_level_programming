#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__"""
        super().__init__(size, size, x, y)

    @property
    def size(self):
        """size"""
        return self.size

    @size.setter
    def size(self, value):
        """size"""
        self.width = value
        self.height = value
