#!/usr/bin/python3
""" class User"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String


class User(BaseModel, Base):
    """class that represents user
    Atrributes:
        __tablename__: name for sql table
        email: user email address.
        passwd: user's password.
        f_name: user's first name
        l_name: user's last name
        places: user-pace relationship
        reviews: user-review"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        passwd = Column(String(128), nullable=False)
        f_name = Column(String(128), nullable=True)
        l_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
