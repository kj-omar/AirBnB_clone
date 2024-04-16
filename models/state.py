#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv


class State(BaseModel, Base):
    """
    Represents a state in the HBNB project.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            from models import storage
            cities = []
            for city in storage.all().values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
