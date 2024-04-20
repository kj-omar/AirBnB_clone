#!/usr/bin/python3
<<<<<<< HEAD
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
=======
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models import storage_type
>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
=======
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
=======
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
<<<<<<< HEAD

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
=======
>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
