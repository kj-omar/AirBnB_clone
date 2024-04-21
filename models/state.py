#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        # Getter to return list of cities

        if getenv('HBNB_TYPE_STORAGE') != 'db':
            from models import storage
            from models.city import City

            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
