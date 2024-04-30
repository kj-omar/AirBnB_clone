#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
import sqlalchemy
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(Integer(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(datetime, nullable=False, default=datetime.utcnow())
    updated_at = Column(datetime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        # if not kwargs:
        #    from models import storage
        #    self.id = str(uuid.uuid4())
        #    self.created_at = datetime.now()
        #    self.updated_at = datetime.now()
        #    storage.new(self)
        # else:
        #    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
        #                                             '%Y-%m-%dT%H:%M:%S.%f')
        #    kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
        #                                             '%Y-%m-%dT%H:%M:%S.%f')
        #   del kwargs['__class__']
        #    self.__dict__.update(kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        if "id" not in kwargs:
            self.id = str(uuid4())
        if "created_at" not in kwargs:
            self.created_at = datetime.utcnow()
        if "updated_at" not in kwargs:
            self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        try:
            del dictionary['_sa_instance_state']
        except KeyError:
            pass

        return dictionary

    def delete(self):
        from models import storage
        del storage
