#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents a state in the HBNB project.
    """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
        name = Column(String(128), nullable=False)
    else:
        name = ""

        @property
        def cities(self):
            """ Returns list of cities according to state.id"""
            cities = models.storage.all(city)
            data = []
            for city in cities:
                if city.state_id == self.id:
                    data.append(city)
            return data
