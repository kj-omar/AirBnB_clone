#!/usr/bin/python3
"""Database Storage Management for AirBnB
Connects to the MySQL database and provides functions to interact
with the data using SQLAlchemy. This class employs a single database
session for efficiency and manages the connection to the engine.
"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """Facilitates interactions with the MySQL database.
    Attributes:
        __engine (sqlalchemy.engine.Engine): The underlying connection to the
                        database.
        __session (sqlalchemy.orm.session.Session): The current active database
                        session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the connection to the MySQL database."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieves all or specific objects from the database.
        Args:
            cls (class, optional): The class of objects to retrieve.
                If None, returns all classes. Defaults to None.

        Returns:
            dict: A dictionary containing the retrieved objects in the format
                <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Schedules an object to be added to the database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all pending changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Schedules an object to be removed from the database session.
        Args:
            obj (object, optional): The object to be deleted. Defaults to None
            (no deletion).
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all database tables (if needed) and starts a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Terminates the current database session."""
        self.__session.close()
