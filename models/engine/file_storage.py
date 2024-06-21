#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a list of objects of one type of class"""
        newDic = {}
        if cls:
            for key, value in FileStorage.__objects.items():
                if value.__class__ == cls:
                    newDic[key] = value
            return newDic
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
            for key, val in temp.items():
                self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def get_reviews(self, place_id):
        """Stores objects in a dictionary with keys based on class and ID.
        Directly access reviews under the key Location"""
        reviews = []
        if f"Review.{place_id}" in self._objects:
            reviews = self._objects[f"Review.{place_id}"]
        return reviews

    """def get_reviews(self, place_id):
        Returns a list of Review objects associated with a Place object
        Args:
            place_id (int): The ID of the Place object
        Returns:
            list: A list of Review objects or an empty list if none found

        all_objects = self.all()  # Get all objects
        reviews = []
        for obj in all_objects.values():
            if isinstance(obj, Review) and obj.place_id == place_id:
                reviews.append(obj)
        return reviews
        otra opcion de la misma def get_reviews(self, place_id)"""
