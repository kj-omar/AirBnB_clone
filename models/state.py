#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
import os


class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128),
                    nullable=False)
        cities = relationship("City",
                            back_populates="state",
                            cascade="all, delete")
    else:
        name = ''

    if not os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            """ getter attribut for FileStorage linked
            between State and City """
            list_city = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
