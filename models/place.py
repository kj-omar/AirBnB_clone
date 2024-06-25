#!/usr/bin/python3
"""
Place Module - contains the Place class
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    """
    Place class inherits from BaseModel and Base.
    Represents a place in the system.
    """

    __tablename__ = 'places'

    reviews = relationship('Review', cascade='all, delete-orphan', backref='place')

    def __init__(self, *args, **kwargs):
        """
        Initializes Place object.
        """
        super().__init__(*args, **kwargs)

