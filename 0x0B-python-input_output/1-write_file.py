#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written.
    :param filename: The name of the file to write. Default is an empty string.
    :param text: The string to write to the file. Default is an empty string.
    :return: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
