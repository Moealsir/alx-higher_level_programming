#!/usr/bin/python3

"""
Base module
"""


class Base:
    """
    Base - Add a brief here.
    """

    def __init__(self, id=None):
        """
        __init__ - Add a brief here.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
