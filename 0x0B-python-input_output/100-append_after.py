#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.
    :param filename: The name of the file to modify. Default is an empty string.
    :param search_string: The string to search for in the file. Default is an empty string.
    :param new_string: The string to insert after each line containing the search string. Default is an empty string.
    """
    lines_to_insert = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if search_string in line:
            lines_to_insert.append(new_string)
            lines_to_insert.append(line)
        else:
            lines_to_insert.append(line)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines_to_insert)
