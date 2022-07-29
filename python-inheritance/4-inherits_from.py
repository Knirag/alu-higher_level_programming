#!/usr/bin/python3
""" Defines the function """


def inherits_from(obj, a_class):
    """
    :param obj and a_class
    :return
    """
    return type(obj) is not a_class and isinstance(obj, a_class)


if __name__ == '__main__':
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
