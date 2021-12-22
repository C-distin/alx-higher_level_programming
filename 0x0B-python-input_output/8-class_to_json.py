#!/usr/bin/python3
"""
function that returns dictionary description with simple data structure for
JSON serialization of an object
"""

# import modules
import json


def class_to_json(obj):
    """
    function that returns dictionary description with simple data structure
    for JSON serialization of an object
    """
    return obj.__dict__
