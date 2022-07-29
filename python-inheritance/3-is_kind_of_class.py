#!/usr/bin/python3
"""Defines the function."""
def is_kind_of_class(obj, a_class):
    """Check if the object is a class instance 
    """
    if isinstance(obj, a_class):
        return True
    return False
