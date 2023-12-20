#!/usr/bin/python3
import math
"""magic class

Raises:
    TypeError: TypeError
"""


class MagicClass:
    """Class that defines a magic class.
    Attributes:
    radius (int): The radius of the circle.
    Methods:
    area(): Calculate the area of the circle.
    circumference(): Calculate the circumference of the circle.
    """

    def __init__(self, radius=0):
        """Initialize the class with a radius.
        Args:
        radius (int): The radius of the circle. Defaults to 0.
        Raises:
        TypeError: If radius is not an integer or float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle.
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Calculate the circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
