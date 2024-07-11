#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

class State(BaseModel, Base):
    """ State class """
    # for database storage
    if models.HBNB_TYPE_STORAGE == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    # for json file storage
    else:
        from models import storage

        name = ""

        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

