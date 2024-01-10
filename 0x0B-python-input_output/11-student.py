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

    def to_json(self, attrs=None):
        """
        whew
        """
        obj = self.__dict__.copy()
        if type(attrs) is not str:
            for item in attrs:
                if type(item) is not str:
                    return obj
        
        d_list = {}
        
        for iatr in range(len(attrs)):
            for satr in obj:
                d_list[satr] = obj[satr]
        return d_list
    
    def reload_from_json(self, json):
        """
        whew
        """
        for atr in json:
            self.__dict__[atr] = json[atr]
