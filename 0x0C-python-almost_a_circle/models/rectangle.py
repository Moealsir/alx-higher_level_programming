#!/usr/bin/python3
from models.base import Base
"""
Rectangle(Base) module
"""


class Rectangle(Base):
    """
    Rectangle(Base) - Add a brief here.
    """


    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ - Add a brief here.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area - Add a brief here.
        """
        return self.width * self.height

    def display(self):
        """
        display - Add a brief here.
        """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')

    def __str__(self):
        """
        __str__ - Add a brief here.
        """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)
        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """
        update - Add a brief here.
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        to_dictionary - Add a brief here.
        """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}
        for key in list_atr:
            dict_res[key] = getattr(self, key)
        return dict_res
