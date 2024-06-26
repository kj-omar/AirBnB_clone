#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

db_type = getenv('HBNB_TYPE_STORAGE')
if db_type == "db":
    Base = declarative_base()
else:
    Base = object

format = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """A base class for all hbnb models"""

    if db_type == "db":
        id = Column(String(60), primary_key=True, unique=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, format)
                if key != "__class__":
                    setattr(self, key, val)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        string = "[{}] ({}) {}".format(
                                type(self).__name__, self.id, self.__dict__)
        return(string)

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return(dictionary)

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
