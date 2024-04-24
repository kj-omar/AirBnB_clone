#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from models import storage
from models.base_model import Base, BaseModel
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(
        String(length=60),
        ForeignKey('cities.id'),
        nullable=False
    )
    user_id = Column(
        String(length=60),
        ForeignKey('users.id'),
        nullable=False
    )
    name = Column(
        String(length=128),
        nullable=False
    )
    description = Column(
        String(length=1024),
        nullable=True
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
        nullable=True
    )
    longitude = Column(
        Float,
        nullable=True
    )
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref=backref('place'), cascade='all, delete')

    elif getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def reviews(self):
            """Returns list of reviews of a place"""
            from models.review import Review
            my_reviews = []
            all_reviews = storage.all(Review)
            for v in all_reviews.values():
                if v['place_id'] == self.id:
                    my_reviews.append(v)
            return (my_reviews)
