#!/usr/bin/python3
"""State Module for HBNB project
This module defines the `State` class representing a state in the application.
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """Represents a state in the application.

    Attributes:
        name (str): The name of the state. (Required)
        cities (list[City], read-only): List of City instances belonging
        to the state.
    """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """Retrieves the list of City instances belonging to the state.

            Returns:
                list[City]: A list of City instances.
            """
            the_cities = []
            for c in models.storage.all(City).values():
                if c.state_id == self.id:
                    the_cities.append(c)
            return the_cities