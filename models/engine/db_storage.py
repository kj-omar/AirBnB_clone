#!/usr/bin/python3
"""
Module defines class for defining mysql storage engine
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from os import getenv


class DBStorage:
    """
    MySQL sqlalchemy mappped class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Instaniates a DBStorage object
        """

        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        hostname = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        _env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(user, password, hostname, database),
            pool_pre_ping=True, echo=True
        )

        if _env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Returns all objects of type cls in db
        """
        from models.city import City
        from models.state import State
        from models.review import Review
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place
        __models = [User, Place, Amenity, City, Review, State]
        cls_objs_dict = {}
        if cls is None:
            for _cls in __models:
                all_objs = self.__session.query(_cls)
                for _obj in all_objs:
                    key = f"{str(_cls)}.{_obj.id}"
                    cls_objs_dict[key] = _obj
        else:
            all_objs = self.__session.query(cls)
            for _obj in all_objs:
                key = f"{str(cls)}.{_obj.id}"
                cls_objs_dict[key] = _obj

        return (cls_objs_dict)

    def new(self, obj):
        """
        Adds obj to current db session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commits all changes to current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from current db session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all table in db
        """
        from models.city import City
        from models.state import State
        from models.review import Review
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        Base.metadata.create_all(self.__engine)

        session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = session()
