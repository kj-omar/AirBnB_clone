#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv

env = getenv('HBNB_TYPE_STORAGE')


place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
        primary_key=True)                      
)


class Place(BaseModel, Base):
    """Place model for HBNB"""
    if env == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=True)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity", backref="place_amenities", viewonly=False)
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
        reviews = []
        amenities = []

        @property
        def reviews(self):
            """Getter for reviews"""
            from models.review import Review
            return [review for review in Review.all() if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter for amenities"""
            from models.amenity import Amenity
            return [Amenity.all()[id] for id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Setter for amenities"""
            from models.amenity import Amenity
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
