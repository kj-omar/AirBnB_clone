#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    __tablename__ = "users"

    email = Column(
        String(length=128),
        nullable=False
    )

    password = Column(
        String(length=128),
        nullable=False
    )

    first_name = Column(
        String(length=128),
        nullable=False
    )

    last_name = Column(
        String(length=128),
        nullable=False
    )
