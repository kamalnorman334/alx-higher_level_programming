#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Return the sum of a and b as an integer
    return int(a) + int(b)

if __name__ == "__main__":
    # Test cases
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    
    # Exception handling for invalid input types
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)

