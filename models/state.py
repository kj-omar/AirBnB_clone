#!/usr/bin/python3
""" State Module for HBNB project """

import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """
    Defines the class State
    """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """
            getter attribute for city objects.
            """
            reloaded_list = models.storage.all("City").values()
            cities_list = []
            for city in reloaded_list:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

    def __init__(self, *args, **kwargs):
        """initializes state object"""
        super().__init__(*args, **kwargs)
