#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    name = ""

    # Association table for Many-to-Many relationship between Place and Amenity
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    # Many-to-Many relationship with Place using place_amenity table
    place_amenities = relationship("Place", secondary=place_amenity, back_populates="amenities")
