#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_engine
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_engine == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

    if storage_engine != 'db':
        @property
        def cities(self):
            """ Getter attribute that returns the list of City instances """
            from models import storage
            from models.city import City
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
