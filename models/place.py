#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import backref, relationship
from models.base_model import Base, BaseModel
from os import getenv

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', ForeignKey('amenities.id'), primary_key=True)
)


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
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)

    elif getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def reviews(self):
            """Returns list of reviews of a place"""
            from models.review import Review
            from models import storage
            my_reviews = []
            all_reviews = storage.all(Review)
            for v in all_reviews.values():
                if v['place_id'] == self.id:
                    my_reviews.append(v)
            return (my_reviews)

        @property
        def amenities(self):
            """Returns list of amenities of a place"""
            from models import storage
            from models.amenity import Amenity
            my_amenities = []
            all_amenities = storage.all(Amenity)
            for _id in self.amenity_ids:
                k = f"Amenity.{_id}"
                my_amenities.append(all_amenities[k])
            return (my_amenities)

        @amenities.setter
        def amenities(self, obj):
            """Appends Amenity.id to amenity_ids"""
            from models import storage
            if obj.__class__.__name__ != 'Amenity':
                pass
            else:
                from models.amenity import Amenity
                all_amenities = storage.all(Amenity)
                for v in all_amenities.values():
                    if v['place_id'] == self.id:
                        self.amenity_ids.append(v.id)
