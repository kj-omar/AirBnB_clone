#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storage_type
from models import storage

class State(BaseModel, Base):
    """ State class """

    if storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """getter docuemnt"""
            citiesList = []
            citiesAll = storage.all(City)
            for city in citiesAll.values():
                if city.state_id == self.id:
                    citiesList.append(city)
            return citiesList