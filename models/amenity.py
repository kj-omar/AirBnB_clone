#!/usr/bin/python3
""" Anenity class definition """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """Represents an amenity offered by places in the application.

    Attributes:
        name (str): The name of the amenity. (Required)
        place_amenities (list[Place], read-only): List of Place instances
        associated with the amenity. (Many-to-Many)
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                        viewonly=False)
    else:
        name = ""