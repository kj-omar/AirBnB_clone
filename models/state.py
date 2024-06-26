#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import shlex


class State(BaseModel, Base):
    """ State class that inherits from BaseModel and Base"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", 
                          cascade="all, delete, delete-orphan"
                          )
    @property
    def cities(self):
        """Getter attribute cities that returns the list of
        City instances with state_id equals to the current 
        State.id"""
        from models import storage
        from models.city import City
        var = storage.all()
        mylist = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                mylist.append(var[key])
        for elem in mylist:
            if elem.state_id == self.id:
                result.append(elem)
        return result
