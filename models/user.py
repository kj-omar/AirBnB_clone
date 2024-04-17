#!/usr/bin/python3
"""User Module for HBNB project
This module defines the `User` class representing a user in the application.
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship
from os import getenv



class User(BaseModel, Base):
    """Represents a user in the application.

    Attributes:
        email (str): Email address of the user. (Required)
        password (str): Password of the user. (Required)
        first_name (str, optional): First name of the user.
        last_name (str, optional): Last name of the user.
        reviews (list[Review], read-only): List of Review instances by the
                                        user.
        places (list[Place], read-only): List of Place instances owned by the
                                        user.
    """
    __tablename__ = 'users'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review", backref="user",
                           cascade="all, delete, delete-orphan")

        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""