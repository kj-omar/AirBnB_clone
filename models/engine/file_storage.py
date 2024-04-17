#!/usr/bin/python3
"""File Storage Management System
Provides an abstraction layer for storing and retrieving application objects.
Uses JSON format to serialize and deserialize data to a file.
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Facilitates object persistence using a JSON file.
    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary holding all instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Retrieves all or specific objects from storage.
        Args:
            cls (class, optional): The class of objects to retrieve.
                If None, returns all objects. Defaults to None.

        Returns:
            dict: A dictionary containing the retrieved objects.
                If a class is specified, only objects of that class are
                returned.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Schedules an object to be added to the storage."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes all objects in storage to the JSON file."""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Loads objects from the JSON file back into storage
        (if it exists).
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Schedules an object to be removed from storage (if it exists)."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Reloads objects from the JSON file on program termination."""
        self.reload()
