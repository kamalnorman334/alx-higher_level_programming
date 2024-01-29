#!/usr/bin/python3
class Rectangle:
    """Class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with specified width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If width is not an int.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If height is not an int.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

