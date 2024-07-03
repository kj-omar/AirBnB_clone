#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import HBNB_TYPE_STORAGE

class Amenity(BaseModel, Base):
    """Amenity class to store amenity information"""
    # for database storage
    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                    viewonly=False)
    # for json file storage
    else:
        name = ""
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
