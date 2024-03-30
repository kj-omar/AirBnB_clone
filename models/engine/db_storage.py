#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        connection = (f'mysql+mysqldb://{user}:{password}@{host}/{db}')
        self.__engine = create_engine(connection, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a given class from the database"""
        all_classes = {
            "State": State,
            "City": City,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity
        }

        objs = {}
        for class_name in all_classes:
            if (cls is None or
                    cls == class_name or
                    cls == all_classes[class_name]):
                for obj in self.__session.query(all_classes[class_name]).all():
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    objs[key] = obj
        return objs

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database session"""
        Base.metadata.create_all(self.__engine)
        engine_bind = {'bind': self.__engine}
        session_factory = sessionmaker(**engine_bind, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
