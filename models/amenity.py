#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """Defines an amenity"""
    __tablename__ = "amenities"
    name = Column(
        String(length=1024),
        nullable=False
    )
