#!/usr/bin/python3
"""
Base class for all models
"""

import json
import csv
import os


class Base:
    """
    Base class for all models
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        converts a list of dictionaries to a json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
