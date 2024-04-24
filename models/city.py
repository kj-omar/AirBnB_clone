#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm.properties import ForeignKey
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(
        String(length=60),
        ForeignKey("states.id"),
        nullable=False
    )

    name = Column(
        String(length=128),
        nullable=False
    )

    state_id = Column(
        String(length=60),
        ForeignKey("states.id"),
        nullable=False
    )

    places = relationship('Place', backref=backref('city'), cascade='all, delete')
