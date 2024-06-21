#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float, event
from sqlalchemy.orm import relationship
from models.review import Review
import models


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, default=None)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        viewonly=False)

    reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete-orphan")

    @property
    def reviews(self):
        """ Getter that that returns the list of Reviews instances """
        instances = models.storage.all(Review)
        new = []
        for review in instances.values():
            if review.place_id == (self.id):
                new.append(review)
        return new


@event.listens_for(Place.amenities, "append")
def on_amenities_apped(target, value, _):
    target.amenity_ids.append(value.id)
