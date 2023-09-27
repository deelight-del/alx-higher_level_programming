#!/usr/bin/python3

"""This file is going to contain the class definition of
Square and its respective attributes
This is module that will contain the class defintion of the
Square class for creatting classes.
"""


class Square:
    """Square A class that abstracts the data
    square.

    Takes no attribute for now.

    It also does not return anything or take any method
    """
    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize the size of
        a square

        Args:
            self: Object reference to itself
            size: size of the square.

        Return:
            Nothing
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """poperty definition of size to return the private method
        that was set by the size setter decorator.

        Args:
            self: The object instantiation within the class def

        Return:
            Private attribute.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Function size that is within the size setter decoration.

        Args:
            self: The object instance of the class.
            size: The size attribute of the object.

        Return:
            Nothing
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """function to define the property of the
        given attribut postion.

        Args:
            self: object self referencing.
        """
        return self.__position

    @position.setter
    def position(self, position):
        """function that sets the attribute position.

        Args:
            self: Object referencing
            position: passing position into the setter option.
        """
        if (not (isinstance(position, tuple))) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Function to calculate the area of a square
        giveUUU
        Args:
            self: The instance of this class

        Return:
            An integer value. The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Function to print a square

        Args:
            self: object instantiaition in class definition.

        Return:
            Nothing.
        """
        if self.__size == 0:
            print()

        else:
            for i in range(0, self.__size):
                for y in range(0, self.__position[1]):
                    if i == 0:
                        print()
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """Function for simple print and formatting text
        for users.

        Args:
            self: The object referencing itself

        Return:
            Nothing.
        """
        list_repr = []
        if self.__size == 0:
            pass
        else:
            for i in range(0, self.__size):
                for y in range(0, self.__position[1]):
                    if i == 0:
                        list_repr.append("\n")
                for x in range(0, self.__position[0]):
                    list_repr.append(" ")
                for j in range(0, self.__size):
                    list_repr.append("#")
                if (i != self.__size - 1):
                    list_repr.append("\n")
        return ("".join(list_repr))
