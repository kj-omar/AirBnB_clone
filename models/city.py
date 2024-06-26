#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ 
    The City class represents a city in the AirBnB clone project.
    
    Attributes:
        __tablename__ (str): Name of the database table for cities.
        state_id (str): ID of the state that the city belongs to.
        name (str): The name of the city.
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
