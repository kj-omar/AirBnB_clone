#!/usr/bin/python3
""" Database storage for airbnb project
here we can see the magic of ORM
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """ This class manages dbstorage for airbnb project """
    __engine = None
    __session = None

    def __init__(self):
        """ this class constructor """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}:3306/{db}',
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query on current db session """
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        new_dict = {}
        classes = {
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
            }
        if cls:
            # becouse cls is string when we passed it as arg
            filter_query = self.__session.query(cls).all()
            for obj in filter_query:
                key = f"{obj.__class__.__name__}.{obj.id}"
                new_dict[key] = obj
        else:
            for key, value in classes.items():
                filter_query = self.__session.query(value).all()
                for obj in filter_query:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        print(new_dict)
        return new_dict

    def new(self, obj):
        """ add obj to db session """
        self.__session.add(obj)

    def save(self):
        """ save changes to db permanently """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj(row) from db """
        if obj is not None:
            self.__session.delete()

    def reload(self):
        """ create tables in the Database """
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        SessionFactory = scoped_session(sessionmaker(bind=self.__engine,
                                      expire_on_commit=False))
        self.__session = SessionFactory()
