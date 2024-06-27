#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete")

    if not os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            """ getter attribut for FileStorage r/n
            between State and City """
            list_city = []
            for _, value in storage.__objects.items():
                if State.id == value.state_id:
                    list_city.append(value)

            return list_city