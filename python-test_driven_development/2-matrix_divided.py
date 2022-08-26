#!/usr/bin/python3
""" matrix module """


def matrix_divided(matrix, div):
    """
    :param matrix: ints/floats in lists
    :param div: which divides the matrix
    :return: new matrix, a result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elements of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    len_e = 0

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError("Each row of the matrix must have the same size")

        if len_e != 0 and len(elems) != len_e:
            raise TypeError("Each row of the matrix must have the same size")

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg)

        len_e = len(elems)
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return m
