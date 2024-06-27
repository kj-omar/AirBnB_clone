#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.place import Place


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
