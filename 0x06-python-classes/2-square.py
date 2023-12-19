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

