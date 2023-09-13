#!/usr/bin/python3
"""
a class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age
"""


class Student:
    """A class student"""
    def ___init__(self, first_name, last_name, age):
        """Initialization of class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=none):
        """A dictionary rep of student instance"""
        if type(attr) == list:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)
        return self.__dict__
