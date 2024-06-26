#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    __tablename__ = "amenities"


    if getenv("HBNB_TYEP_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
