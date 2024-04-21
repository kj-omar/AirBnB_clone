#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy.orm import relationship
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(
        String(length=128),
        nullable=False
    )

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',cascade='all, delete-orphan')

    else:
        @property
        def cities(self):
            """
            Returns cities related to a state
            """
            all_cities = []
            dict = storage.all(State)
            for v in dict.values():
                if v.state_id == self.id:
                    all_cities.append(v)
            return (all_cities)
