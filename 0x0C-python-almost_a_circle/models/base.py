#!/usr/bin/python3
"""
Module for the Base class
"""


class Base:
    """
    The Base class

    Attributes:
        __nb_objects (int): A private class attribute.
        id (int): A public instance attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): An optional identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
