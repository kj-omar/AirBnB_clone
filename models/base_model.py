#!/usr/bin/python3
"""Base class for all hbnb models, providing core data management."""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String


Base = declarative_base()


class BaseModel:
    """Core data object for hbnb, offering lifecycle management.

    Attributes:
        id (str): Unique identifier (UUID). (Primary Key)
        created_at (datetime): Creation timestamp (UTC).
        updated_at (datetime): Last update timestamp (UTC).
    """    
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Initializes a new model instance.

        Args:
            kwargs (dict, optional): Key-value pairs for attributes.
                If not provided, sets id, created_at, and updated_at to
                current values.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
           
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if not self.id:
                self.id = str(uuid4())

    def __str__(self):
        """Returns a string representation of the instance."""
        copy_dict = self.__dict__.copy()
        copy_dict.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, copy_dict)

    def save(self):
        """Updates updated_at and saves the instance."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance.
        Includes type information, formatted timestamps, and removes internal
        attributes.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Deletes the instance from storage."""
        models.storage.delete(self)