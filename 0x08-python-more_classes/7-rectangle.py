#!/usr/bin/python3
"""This module contains the
class definition of the class Rectangle and
its respective methods, and attributes.
"""


class Rectangle:
    """Class definition of
    Rectangle, including methoda and attributes
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The init mehtod of our class

        Args:
            self: reference to object instance
            width: The width dimension passed into creating the object.
            height: The height dimension passed into creating the object.

        Return:
            None.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property of the width object to get the width
        object respectively.
        """
        return self.__width

    @width.setter
    def width(self, w):
        """The accompanying setter function of the property
        width above.
        """
        if type(w) is not int:
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = w

    @property
    def height(self):
        """property getter method for
        reading the height dimension
        """
        return self.__height

    @height.setter
    def height(self, h):
        """setter for the heighr parameter
        or height dimension
        """
        if type(h) is not int:
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = h

    def area(self):
        """Instance method to return the
        area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Instance method to return the
        perimeter of the rectancgle
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Magic method that str function or
        print function uses to reperesents
        info to users.
        """
        final_str = ""
        if (self.__height == 0) or (self.__width == 0):
            return final_str
        for i in range(self.__height):
            for j in range(self.__width):
                final_str = final_str + Rectangle.print_symbol[:]
            if (i != self.__height - 1):
                final_str = final_str + "\n"
        return final_str

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", "\
                + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
