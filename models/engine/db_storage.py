#!/usr/bin/python3
"""Module containing the new engine for hbnb"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage():
    """Storage engine for the hbnb console"""

    __engine = None
    __session = None

    def __init__(self):
        """Method for instantiation"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        print("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pwd, host, db))
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to query the current database session on all objects
        depending on the argument class name passed"""

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        """Add all available instances to a dict"""
        classes = [State, City, User, Place, Review, Amenity]

        """If no class is specified, return all objects in the session.
        If a class is specified, query only for objects of that class
        available in the session"""
        objects = {}

        if not cls:
            for cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    objects[key] = obj
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{type(obj).__name__}.{obj.id}"
                objects[key] = obj

        return objects

    def new(self, obj):
        """Method to add an object to the db session"""

        self.__session.add(obj)

    def save(self):
        """Method to commit all the changes of the current db session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete the obj from the current db sesion"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Used to create the current db session"""


        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        scope = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(scope)
        self.__session = Session()

    def close(self):
        """Method to end a session"""

        self.__session.close()
