#!/usr/bin/python3
"""This module contains the class definiton of the
Base class that our future classes will be inheriting
from.
"""


import json
import csv


class Base:
    """Class definition of Base
    """
    __nb_objects = 0

    @classmethod
    def set_objects(cls, num):
        """Function to set the number of objects to a given number
        of choice - num"""
        Base.__nb_objects = num

    @classmethod
    def create(cls, **dictionary):
        """class method that creates a new instance from the
        keywords of the dictionary argument"""
        if cls.__name__ == 'Rectangle':
            new_object = cls(1, 1)
            new_object.update(**dictionary)
            return new_object
        if cls.__name__ == 'Square':
            new_object = cls(1)
            new_object.update(**dictionary)
            return new_object
        else:
            cls(**dictionary)

    @classmethod
    def load_from_file(cls):
        """The class method to return list of instances that
        are created from a json files corresponding to the class"""
        try:
            with open(cls.__name__ + ".json", mode="r") as f:
                str_json = f.read().rstrip()
            list_of_attrsdict = cls.from_json_string(str_json)
            list_of_instances = []
            if len(list_of_attrsdict) != 0:
                for attrs in list_of_attrsdict:
                    list_of_instances.append(cls.create(**attrs))
                return list_of_instances
            else:
                return []
        except IOError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """The method to convert list_dictionaries to
        a json string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """THis class method loads a list of dictionaries
        which are attributes of a given object, and returns a
        list of dictionaries python object."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """The class method to save a list_objs attributes to a json file
        that is specified by the class name"""
        with open(cls.__name__ + ".json", mode="w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(cls.to_json_string(None))
            else:
                list_of_dicts = []
                for obj in list_objs:
                    list_of_dicts.append(obj.to_dictionary())
                f.write(cls.to_json_string(list_of_dicts))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """The class method to save a list_objs attributes to a csv file
        that is specified by the class name"""
        with open(cls.__name__ + ".csv", mode="w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("")
            else:
                csv_writer = csv.writer(f)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        csv_writer.writerow([obj.id, obj.width, obj.height,
                                            obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        csv_writer.writerow([obj.id, obj.size,
                                            obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """The class method to return list of instances that
        are created from a csv files corresponding to the class"""
        try:
            with open(cls.__name__ + ".csv", mode="r") as f:
                list_of_attrsdict = []
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    if row == "[]":
                        continue
                    attrsdict = dict()
                    if cls.__name__ == "Rectangle":
                        attrsdict["id"] = int(row[0])
                        attrsdict["width"] = int(row[1])
                        attrsdict["height"] = int(row[2])
                        attrsdict["x"] = int(row[3])
                        attrsdict["y"] = int(row[4])
                    elif cls.__name__ == "Square":
                        attrsdict["id"] = int(row[0])
                        attrsdict["size"] = int(row[1])
                        attrsdict["x"] = int(row[2])
                        attrsdict["y"] = int(row[3])
                    list_of_attrsdict.append(attrsdict)
            list_of_instances = []
            if len(list_of_attrsdict) != 0:
                for attrsdict in list_of_attrsdict:
                    list_of_instances.append(cls.create(**attrsdict))
                return list_of_instances
            else:
                return []
        except IOError:
            return []

    def __init__(self, id=None):
        """Init definition of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def id(self):
        """property decorator of the attr id"""
        return self.__id

    @id.setter
    def id(self, id):
        """setter property of the attribute id"""
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
