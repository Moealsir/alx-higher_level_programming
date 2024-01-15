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
            id (int, optional): An optional.
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = type(self).__nb_objects


if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
