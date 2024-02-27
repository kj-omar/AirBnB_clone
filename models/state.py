#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sys
from uuid import uuid4
import shlex
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
