#!/usr/bin/python3
""" urllib.request module"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as file:
        file_1 = file.read()
        print('Body response:')
        print('\t- type: {}'.format(type(file_1)))
        print('\t- content: {}'.format(file_1))
        print('\t- utf8 content: {}'.format(file_1.decode("utf-8")))
