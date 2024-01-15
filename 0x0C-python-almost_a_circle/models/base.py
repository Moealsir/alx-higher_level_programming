#!/usr/bin/python3
""" Module for the Base class """


class Base:
    """ The Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """xConstructor for the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

