#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import orm
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref='state',
                          cascade="all, delete-orphan",
                          passive_deletes=True)

    @property
    def cities(self):
        """ Getter method to retrieve cities for the current State """
        city_list = []

        for obj in storage.all(City):
            if obj.state_id == self.id:
                city_list.append(obj)
        return city_list

    if getenv("HBNB_TYPE_STORAGE") != "db":
        """Existing code for non-database storage remains here"""
        pass
