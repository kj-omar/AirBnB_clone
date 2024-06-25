#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"
    
    name = Column(String(128), nullable=False)

    # Define the many-to-many relationship with Place
    place_amenities = relationship(
        "Place",
        secondary=place_amenity,
        back_populates="amenities",
        viewonly=False
    )

