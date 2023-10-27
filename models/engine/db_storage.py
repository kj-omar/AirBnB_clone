#!/usr/bin/python3
""" DBStorage Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """ DBStorage class doc"""
    __engine = None
    __session = None

    def __init__(self):
        """The constructor method"""
        env_user = getenv("HBNB_MYSQL_USER")
        env_pass = getenv("HBNB_MYSQL_PWD")
        env_host = getenv("HBNB_MYSQL_HOST", default="localhost")
        env_db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(f"mysql+mysqldb://{env_user}:\
                                      {env_pass}@{env_host}\
                                        /{env_db}", pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session """
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__session.query(cls)
        else:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())
        obj_dict = {}
        for obj in objects:
            obj_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return obj_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database
        and creates the current database session"""
        Base.metadata.create_all(self.__engine)
        session_exp = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_exp)
        self.__session = Session()

    def close(self):
        """Closing the session"""
        self.__session.close()
