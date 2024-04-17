#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    __tablename__ = "places"

    city_id = Column(
        String(length=60),
        ForeignKey("cities.id"),
        nullable=False
    )

    user_id = Column(
        String(length=60),
        ForeignKey("cities.id"),
        nullable=False
    )

    name = Column(
        String(length=128),
        nullable=False
    )

    description = Column(
        String(length=1024),
        nullable=False
    )

    number_rooms = Column(
        Integer,
        nullable=False,
        default=0
    )

    number_bathrooms = Column(
        Integer,
        nullable=False,
        default=0
    )

    max_guest = Column(
        Integer,
        nullable=False,
        default=0
    )

    price_by_night = Column(
        Integer,
        nullable=False,
        default=0
    )

    latitude = Column(
        Float,
        nullable=False
    )

    longitude = Column(
        Float,
        nullable=False
    )
