#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_engine
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel):
    """ The Amenity class, contains name """
    __tablename__ = 'amenities'
    if storage_engine == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place',
                                       secondary=place_amenity,
                                       back_populates='amenities')
    else:
        name = ""
