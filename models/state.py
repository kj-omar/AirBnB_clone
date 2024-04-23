#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import String, Column
from sqlalchemy.orm import backref, relationship
from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(
        String(length=128),
        nullable=False
    )

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref=backref('state'), cascade='all, delete')

    elif getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            """
            Returns all cities linked to state
            """
            from models.city import City
            from models import storage
            all_cities = []
            dictionary = storage.all(City)
            for k in dictionary.values():
                if k['state_id'] == self.id:
                    all_cities.append(k)

            return (all_cities)
