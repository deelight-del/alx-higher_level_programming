#!/usr/bin/python3
"""This module contains the class definition of the
Rectangle class that inherits from the Base Class"""


from models.base import Base


class Rectangle(Base):
    """This begins the class defintion of the Rectangle
    class that inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The init class of the class for construction."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property function definiton of the attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """property setter for the width attribute of the class
        instance"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """property function definiton of the attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """property setter for the height attribute of the class
        instance"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """property function definiton of the attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """property setter for the x attribute of the class
        instance"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """property function definiton of the attribute y"""
        return self.__y

    @y.setter
    def y(self, y):
        """property setter for the y attribute of the class
        instance"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Method to caluculate the area of a given object"""
        return self.__width * self.__height

    def display(self):
        """The method for displaying a given Rectangle
        object"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Special method `__str__` that will be used
        for end user display and the respective function"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,\
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """The method that uses no-keyword and keyword
        variable length of ordered and keyed argument to update
        the attributes of a given instance of this class"""
        lst_args = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i < len(lst_args):
                    setattr(self, lst_args[i], arg)
        else:
            if kwargs is not None:
                for key, val, in kwargs.items():
                    if key in lst_args:
                        setattr(self, key, val)
