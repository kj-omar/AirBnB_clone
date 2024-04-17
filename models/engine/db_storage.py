#!/usr/bin/python3
"""
Module creates a MySQL database engine
"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import column, create_engine
from models.base_model import Base
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """
    Class responsible for mysql storage
    """
    __engine = None
    __session = None
    __classes = [City, User, Place, State, Review, Amenity]

    def __init__(self) -> None:
        """
        Instantiates a DBStorage object
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        hostname = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        _env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, password, hostname, database),
            pool_pre_ping=True
        )
        if _env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries db for objects of type cls
        """
        cls_objs_dict = {}
        if cls is None:
            for _cls in self.__classes:
                all_objs = self.__session.query(_cls)
                for _obj in all_objs:
                    print(f"Bruh I tried with {_obj.__str__()}")
                    k = f"{_cls}.{_obj.id}"
                    cls_objs_dict[k] = _obj
        else:
            all_objs = self.__session.query(eval(cls))
            for _obj in all_objs:
                k = f"{cls}.{_obj.id}"
                cls_objs_dict[k] = _obj
        return cls_objs_dict

    def new(self, obj):
        """
        Adds obj to current db
        """
        self.__session.add(obj)
        self.save()

    def save(self):
        """
        Commits all changes to current db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj to current db
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in current db
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(
                autoflush=False,
                autocommit=False,
                expire_on_commit=False,
                bind=self.__engine
            )
        )
        self.__session = Session()
