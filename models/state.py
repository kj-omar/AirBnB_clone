#!/usr/bin/python3
""" State Module for HBNB project """

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

        @property
        def cities(self):
            """
            """
            variable = models.storage.all()
            temp_list = []
            result = []
            for key in variable:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    temp_list.append(variable[key])
            for element in temp_list:
                if (element.state_id == self.id):
                    result.append(element)
                return(result)
    else:
        name = ""
