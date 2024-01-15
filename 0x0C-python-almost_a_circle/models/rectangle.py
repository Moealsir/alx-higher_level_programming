#!/usr/bin/python3

"""
Rectangle(Base) module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle(Base) - Add a brief here.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ - Add a brief here.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width - Add a brief here.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width - Add a brief here.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height - Add a brief here.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height - Add a brief here.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x - Add a brief here.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x - Add a brief here.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y - Add a brief here.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y - Add a brief here.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
