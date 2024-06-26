#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
            """Returns a string representation of the instance.

            Returns:
                str: A string representation of the instance.
            """
            obj_str = "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
            )
            return obj_str

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
            """Converts the instance into a dictionary format.

            Returns:
                dict: A dictionary representation of the instance.
            """
            obj_dict = self.__dict__.copy()
            obj_dict['__class__'] = self.__class__.__name__
            
            for k, v in obj_dict.items():
                if isinstance(v, datetime):
                    obj_dict[k] = v.isoformat()
            return obj_dict
