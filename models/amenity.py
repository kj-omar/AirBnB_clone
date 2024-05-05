#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Defines an amenity"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(
            String(length=1024),
            nullable=False
        )

        place_amenities = relationship(
            'Place',
            secondary=place_amenity,
            overlaps='amenities'
        )

    else:
        name = ""
