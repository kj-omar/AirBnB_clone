#!/usr/bin/python3
"""
User Module - contains the User class
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """
    User class inherits from BaseModel and Base.
    Represents a user of the system.
    """

    __tablename__ = 'users'

    reviews = relationship('Review', cascade='all, delete-orphan', backref='user')

    def __init__(self, *args, **kwargs):
        """
        Initializes User object.
        """
        super().__init__(*args, **kwargs)

