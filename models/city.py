#!/usr/bin/python3
"""City Module for HBNB project
This module defines the `City` class representing a city in the application.
"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """Represents a city in the application.

    Attributes:
        name (str): The name of the city. (Required)
        state_id (str): The ID of the associated state. (Required)
        places (list[Place], read-only): List of Place instances belonging
        to the city.
    """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")


    else:
        state_id = ""
        name = ""