#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    name = ""

    __tablename__ = "amenities"

    name = Column(
        String(length=128),
        nullable=False
    )
