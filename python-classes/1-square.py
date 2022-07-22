#!/usr/bin/python3
"""NO MODULES USED IN THIS CODE"""


class Square:
    """The Class defines the sizes of a square
    and show any errors and exceptions"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.square_size = size
