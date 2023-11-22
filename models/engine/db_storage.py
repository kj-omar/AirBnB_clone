#!/usr/bin/python3
"""database storage engine"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapper


user = os.environ['HBNB_MYSQL_USER'] if 'HBNB_MYSQL_USER' in os.environ else None
password = os.environ['HBNB_MYSQL_PWD'] if 'HBNB_MYSQL_PWD' in os.environ else None
host = os.environ['HBNB_MYSQL_HOST'] if 'HBNB_MYSQL_HOST' in os.environ else None
database = os.environ['HBNB_MYSQL_DB'] if 'HBNB_MYSQL_DB' in os.environ else None
test = os.environ['HBNB_ENV'] if 'HBNB_ENV' in os.environ else None

class DBStorage():
    """database engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initialisation"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), pool_pre_ping=True)
        if test == 'test':
            Base.metadata.drop_all()

        self.__session = None

    def all(self, cls=None):
        """query on the current database session"""
        if cls:
            rows = self.__session.query(cls).all()
        else:
            all_mapped_cls = [model.class_ for model in mapper(Base).iterate_to_root()]
            rows = [obj for cls in all_mapped_cls for obj in self.__session.query(cls).all()]
            dictionary = {row.id: row for row in rows}
            return dictionary

    def new(self, obj):
        """adds new object to the database"""
        self.__session_add(obj)

    def save(self):
        """commits changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
<<<<<<< HEAD
        """deletes object in the current session"""
        self.__session.delete(obj)
        self.save()

    def reload(self):
        """creates all tables in the database"""
        from models.city import City
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.user import User
        from models.amenity import Amenity
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)

=======
        """deletes"""
>>>>>>> b6e275d5ab8287e73cef6e71bddbed1879d6d3c6
