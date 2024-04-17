#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    name = ""

    __tablename__ = "states"

    name = Column(
        String(length=128),
        nullable=False
    )

    cities = relationship(
        'City',
        backref='state',
        cascade='all, delete-orphan'
    )
