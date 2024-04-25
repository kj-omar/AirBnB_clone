#!/usr/bin/python3
"""
Module defines mysql db wrapped in sqlalchemy orm
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from os import getenv


class DBStorage:
    """
    Module defines db to map classes onto mysqldb
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instaniates a DBStorage instance"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        hostname = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        _env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(user, password, hostname, database),
            pool_pre_ping=True, echo=False
        )

        if _env == 'test':
            Base.metadata.drop_all(bind=self.__engine)
        # db = "sqlite:///socialDB.db"
        # self.__engine = create_engine(db, pool_pre_ping=True)

    def all(self, cls=None):
        """Returns all instances of type"""
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        _classes = [State, City, Place, Amenity, User, Review]
        all_obj = {}
        if self.__session is None:
            self.reload()
        if cls:
            for obj in self.__session.query(cls):
                all_obj[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            for model in _classes:
                for obj in self.__session.query(model):
                    all_obj[obj.__class__.__name__ + "." + obj.id] = obj

        return (all_obj)

    def new(self, obj):
        """Adds obj to current db"""
        if self.__session is None:
            self.reload()
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Commits all changes to current db"""
        if self.__session is None:
            self.reload()
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from current db"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all mapped tables into db and a new session
        """
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )
