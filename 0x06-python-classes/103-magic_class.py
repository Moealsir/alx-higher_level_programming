#!/usr/bin/python3
import math
"""magic class

Raises:
    TypeError: TypeError
"""


class MagicClass:
    """A class that defines a magic circle.

    Attributes:
        radius (int or float): The radius of the circle.

    Methods:
        area(): Calculate the area of the circle.
        circumference(): Calculate the circumference of the circle.

    Raises:
        TypeError: If radius is not an integer or float.
    """

    def __init__(self, radius=0):
        """Initialize the MagicClass with a given radius.

        Args:
            radius (int or float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not an integer or float.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
