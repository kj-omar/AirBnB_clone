#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Definition of class Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialises Amenity """
        super().__init__(*args, **kwargs)
