#!/usr/bin/python3
""" Amenity Module for HBNB project """

import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


class Amenity(BaseModel, Base):
    """ Definition of class Amenity """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialises Amenity """
        super().__init__(*args, **kwargs)
