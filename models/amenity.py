#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    """Amenity class inherits from BaseModel and Base"""

    __tablename__ = 'amenities'  # Table name definition

    name = Column(String(128), nullable=False)  # Column definition for name

    # Many-to-Many relationship with Place via place_amenity table
    place_amenities = relationship("Place", secondary='place_amenity', viewonly=False)

    def __init__(self, *args, **kwargs):
        """Initialization of Amenity Class"""
        super().__init__(*args, **kwargs)

    def places(self):
        """Getter method for places linked with this Amenity"""
        return self.place_amenities


class Amenity(BaseModel):
    name = ""
