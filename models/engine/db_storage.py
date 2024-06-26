#!/usr/bin/python3
"""
DB storage engine class
"""

from os import getenv
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """ Database Storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialises the database engine """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, password,
                                                 host, database)
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns dictionary of all objects or objects of type cls
        """
        if not self.__session:
            self.reload()
        obj_dict = {}
        if type(cls) == str:
            cls = classes.get(cls, None)
        if not cls:
            for cls in classes.values():
                for objs in self.__session.query(cls):
                    obj_dict[objs.__class__.__name__ + "." + objs.id] = objs
        else:
            for objs in self.__session.query(cls):
                obj_dict[objs.__class__.__name__ + "." + objs.id] = objs
        return(obj_dict)

    def new(self, obj):
        """ Creates new object in database """
        self.__session.add(obj)

    def save(self):
        """ Saves current session to database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes object if obj is not None """
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Recreates objects from the database """
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(Session)
