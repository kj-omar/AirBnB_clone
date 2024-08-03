#!/usr/bin/python3
"""
This module defines a class to manage database storage for hbnb clone
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    This class manages storage of hbnb models in a database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the database storage instance
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """
        new_dict = {}
        classes = [User, State, City, Place, Amenity, Review]
        if cls is None:
            for c in classes:
                for obj in self.__session.query(c).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """
        Adds new object to storage session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the database
        """
        if obj is not None:
            self.__session.delete(obj)
        else:
            return

    def reload(self):
        """
        Creates all tables in the database and
        initializes a session to interact
        with the database
        """
        Base.metadata.create_all(self.__engine)
        session_f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_f)
        self.__session = Session()

    def close(self):
        """
        Close the session
        """
        self.__session.close()

    def get(self, cls, id):
        """
        Get an object from the database
        """
        return self.__session.query(cls).get(id)

    def count(self, cls=None):
        """
        Get the count of objects in storage
        """
        return len(self.all(cls))
