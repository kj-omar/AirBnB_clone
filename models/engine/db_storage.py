#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv, environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """DB storage managment Class"""
    __engine = None
    __session = None
    classes = [Amenity, City, Place, Review, State, User]

    def __init__(self):
        """ Initializes class """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
         """Returns a dictionary of models currently in database"""
        objs = []
        data = {}
        if not cls:
            for item in self.classes:
                objs.extend(self.__session.query(item).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()

        for obj in objs:
            data[obj.__class__.__name__ + '.' + obj.id] = obj
        return data

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def reload(self):
        """Reload the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

     def delete(self, obj=None):
        """Deletes obj from the database"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Handles close of DBStorage"""
        self.__session.close()
