#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """
    function
    """
    def area(self):
        """
        parameter self
        raise and exception with a message
        """
        raise Exception("area() is not implemented")


if __name__ == '__main__':
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
