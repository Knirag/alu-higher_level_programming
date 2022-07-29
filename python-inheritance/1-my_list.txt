#!/usr/bin/python3
""" Utilizing no module """


class MyList(list):
    """ Mylist class """

    def print_sorted(self):
        """ Function prints sorted list """
        print(sorted(self))
