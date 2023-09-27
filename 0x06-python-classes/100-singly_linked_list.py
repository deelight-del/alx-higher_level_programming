#!/usr/bin/python3

"""This file is going to contain the class definition of
Node and its respective Singly Linkedlist implementation.
This is module that will contain the class defintion of the
Nodee class for creatting classes.
"""


class Node:

    """The class Node that abstracts the funcionalities
    of a Node
    """

    def __init__(self, data, next_node=None):
        """Initializing method of the class

        Args:
            self: The object reference.
            data: The data to be added to a given Node.

        Return:
            Nothing.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """propety of attribute data
        """
        return self.__data

    @data.setter
    def data(self, data):
        """data setter wrapped to set the data.

        Args:
            self: object reference.
            data: The actual data to be set.

        Return:
            Nothhing.
        """

        if not(isinstance(data, int)):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """property method of next_node.
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """setter function for next_node.
        """
        if (isinstance(next_node, Node)) or (next_node is None):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A data Abstraction of SinglyLinkedList.
    Selah.
    """

    def __init__(self):
        """The init method for initializing a singly
        LinedList
        """
        self.__head = None

    def __str__(self):
        """Function to enable us print what is
        in the given object.

        Args:
            self: object refernce.

        Return:
            Nothing. Just prints.
        """
        if (self.__head):
            str_ls = []
            temp = self.__head
            i = 0
            while (temp):
                str_ls.append(temp.data)
                temp = temp.next_node
            return ('\n'.join(map(str, str_ls)))

    def sorted_insert(self, value):
        """Function that adds a newnode into the sorted position of the
        LinkedList.

        Args:
            self: object reference
            value: The value of the new node
        Return:
            Nothing.
        """
        new_node = Node(value)
        if (self.__head):
            if (value < self.__head.data):
                temp2 = self.__head
                self.__head = new_node
                new_node.next_node = temp2
            else:

                track = self.__head
                while track.next_node:
                    if (value >= track.data and value <= track.next_node.data):
                        temp = track.next_node
                        track.next_node = new_node
                        new_node.next_node = temp
                        break
                    track = track.next_node
                else:
                    track.next_node = new_node

        else:
            self.__head = new_node
