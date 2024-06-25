#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST', 'localhost')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """returning all the related objects of a specific class"""
        all_objs = {}

        if cls:
            for obj in self.__session.query(cls).all():
                all_objs.update({"{}.{}".format(type(obj).__name__, obj.id): obj})
        else:
            for obj in classes.values():
                for value in self.__session.query(obj).all():
                    all_objs.update({"{}.{}".format(type(value).__name__, value.id): value})

        return all_objs
    def new(self, obj):
        """Adding new objects to the databases as rows"""
        self.__session.add(obj)
    
    def save(self):
        """Commiting the whole process to the database"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Deleting a specific object"""
        if obj:
            self.__session.query(type(obj).__name__).filter(id = obj.id).delete()

    def reload(self):
        """Reloading the whole objects and call the metadate 
        to convert all the process to SQL code
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ScopedSession = scoped_session(Session)
        self.__session = ScopedSession()

    def close(self):
        """Closing the session"""
        self.__session.close()       