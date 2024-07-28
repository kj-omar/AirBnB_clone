#!/usr/bin/python3
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a state for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table states.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            list_of_city = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list_of_city.append(city)
            return list_of_city

     def cities(self):
        """Return a list of City objects linked to the current State"""
        if isinstance(storage, DBStorage):
            return [city for city in storage.all(City).values() if city.state_id == self.id]
        else:
            all_cities = storage.all(City).values()
            return [city for city in all_cities if city.state_id == self.id]
