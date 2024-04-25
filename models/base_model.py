#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import getenv
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(
            String(length=60),
            primary_key=True,
            nullable=False
        )
        created_at = Column(
            DateTime,
            nullable=False,
            default=datetime.now()
        )
        updated_at = Column(
            DateTime,
            nullable=False,
            default=datetime.now()
        )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        if not kwargs:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try:
                kwargs["updated_at"] = datetime.fromisoformat(
                    kwargs["updated_at"])
                kwargs["created_at"] = datetime.fromisoformat(
                    kwargs["created_at"])
            except (KeyError, ValueError):
                kwargs["updated_at"] = kwargs["created_at"] = datetime.now()

            self.__dict__["id"] = uuid.uuid4()
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            self.__dict__.update(kwargs)
        storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary = self.__dict__.copy()
        if dictionary['_sa_instance_state']:
            dictionary.pop('_sa_instance_state')
        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def __repr__(self) -> str:
        """Returns an official string representation"""
        return (self.__str__())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        if dictionary['_sa_instance_state']:
            dictionary.pop('_sa_instance_state')
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes an instance from storage"""
        from models import storage
        storage.delete(self)
