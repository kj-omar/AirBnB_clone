"""
This module defines an engine for database storage.
"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {
    'User': User, 'Place': Place,
    'State': State, 'City': City,
    'Amenity': Amenity, 'Review': Review
    }


class DBStorage():
    """
    An engine for database storage.

    Private Class Attributes:
    - __engine
    - __session

    Public Instance Methods:
    - all: Queries all objects in the current database
     session for a specific class name.
    - new: Adds an object to the current database session.
    - save: Commits all changes of the current database session.
    - delete: Deletes an object from the current database session.
    - reload: Creates all tables in the database and creates the
     current database session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        - Creates an engine and links it to a database.
        - Drops all tables if the environment variable
        HBNB_ENV is equal to test.
        """

        db_user = getenv('HBNB_MYSQL_USER')
        db_pwd = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            f'mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_name}',
            pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

