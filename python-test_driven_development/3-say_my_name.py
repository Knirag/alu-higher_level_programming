#!/usr/bin/python3
""" module to print names """


def say_my_name(first_name, last_name=""):
    """
    :param first_name:
    :param last_name: a string
    :return: print first and last name as strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == '__main__':

    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    # say_my_name(77, 7)
    # say_my_name("Clone", 7)
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
