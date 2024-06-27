#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

# AirBnB_clone_v2 imports
from sqlalchemy import Column, String, DateTime, MetaData
from sqlalchemy.orm import declarative_base

# Create Base = declarative_base() before the class definition of BaseModel
Base = declarative_base()


class BaseModel():
    """A base class for all hbnb models"""
    # create variable to store time format
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    # Create class attributes for id, created at
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, self.TIME_FORMAT)
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
        else:
            import models
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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

        # call models.storage.new(self) just before models.storage.save()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Converts the instance into a dictionary format.

        Returns:
            dict: A dictionary representation of the instance.
        """
        # remove the key _sa_instance_state from the dictionary
        if hasattr(self, '_sa_instance_state'):
            delattr(self, '_sa_instance_state')

        # create a dictionary of the instance attributes
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        for k, v in obj_dict.items():
            if isinstance(v, datetime):
                obj_dict[k] = v.isoformat()
        return obj_dict

    def delete(self):
        """
        Delete the current instance from the storage.

        Deletes the current instance from the storage by calling
        the `delete` method of the storage object.
        After deleting the instance, saves the changes to storage.

        Returns:
            None
        """
        from models import storage
        storage.delete(self)
