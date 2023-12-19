#!/usr/bin/python3
"""a module define square class

Raises:
    TypeError: int size
    ValueError: size >= 0
"""


class Square:
    """Class representing a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        area(): Calculate the area of the square.
    """

    def __init__(self, size=0):
        """Initialize square with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def area(self):
        """Calculate the area of the square.
        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

    @size.setter
