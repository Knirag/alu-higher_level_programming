#!/usr/bin/python3
""" module that  prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    :param text: text to be split where (.?:) are
    :return: print a text and a new line where there are (.?:)
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    char = ".?:"
    aux = 0
    for i in text:
        if aux == 0:
            if i == ' ':
                continue
            else:
                print("{}".format(i), end="")
                aux = 1
        else:
            if i in char:
                print("{}".format(i), end="\n\n")
                aux = 0
            else:
                print("{}".format(i), end="")
