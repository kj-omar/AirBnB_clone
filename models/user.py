#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relationship
from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"
        email = Column(
            String(length=128),
            nullable=False,
            unique=True
        )
        password = Column(
            String(length=128),
            nullable=False
        )
        first_name = Column(
            String(length=128),
            nullable=True
        )
        last_name = Column(
            String(length=128),
            nullable=True
        )
        places = relationship(
            'Place',
            backref=backref('user'),
            cascade='all, delete'
        )
        reviews = relationship(
            'Review',
            backref=backref('user'),
            cascade='all, delete'
        )

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
