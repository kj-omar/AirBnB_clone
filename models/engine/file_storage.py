#!/usr/bin/python3
"""module for file storage for AirBnB"""

from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
import shlex
import json
from models.state import State


class FileStorage:
    """class serializes instances to a JSON and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """defines a dictionary
        Return:
            returns dictionary of __object
        """
       """ dict = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dict)"""
        if cls is None:
            return self.__objects
        else:
            return {key:obj for key, in self.__object.items() if insistance(obj, cls)}

    def new(self, obj):
        """sets __object given obj
        params:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete existing element class name
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """closes the session with reload() function
        """
        self.reload()
