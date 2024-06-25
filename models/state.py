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
