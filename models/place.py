#!/usr/bin/python3
"""This module defines the Place class representing a place listing
    and related functions for managing place rentals.
"""
import models
from models import Amenity, Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Represents a place listing.

    Attributes:
        city_id (str): The ID of the associated city.
        user_id (str): The ID of the user who owns the place.
        name (str): Name of the place.
        description (str, optional): Description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests allowed.
        price_by_night (int): Price for a night's stay.
        latitude (float, optional): Geographical latitude of the place.
        longitude (float, optional): Geographical longitude of the place.
        amenity_ids (list): List of Amenity IDs associated with the place.
        reviews (list[Review]): List of reviews for this place.
        amenities (list[Amenity]): List of amenities associated with the
                                place.
    """
    __tablename__ = 'places'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="Place",
                               cascade="all, delete, delete-orphan")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref="place_amenities")
    else:
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

        @property
        def reviews(self):
            review_list = []
            for value in models.storage.all(Review).values():
                if value.place_id == self.id:
                    review_list.append(value)
                return review_list

        @property
        def amenities(self):
            amenity_list = []
            for value in models.storage.all(Amenity).values():
                if value.place_amenity.place_id == self.id:
                    amenity_list.append(value)
                return amenity_list

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)