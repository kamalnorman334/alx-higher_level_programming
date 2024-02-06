#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.
    :param filename: The name of the file to read. Default is an empty string.
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')