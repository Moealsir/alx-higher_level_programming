#!/usr/bin/python3
"""
whew
"""


class Student:
    """
    A class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        whew
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        whew
        """
        return self.__dict__.copy()
