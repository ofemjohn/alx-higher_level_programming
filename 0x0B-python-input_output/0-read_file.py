#!/usr/bin/python3
'''
Contains the text function for reading a text file.

'''


def read_file(filename=""):
    ''' Reading a file from the text file UTF8'''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
