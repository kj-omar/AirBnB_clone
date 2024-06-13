#!/usr/bin/python3
"""Place Module for HBNB project"""


from os import getenv
from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy import Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


"""Association table"""
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """Place class for HBNB project"""
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    """Property methods"""
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def amenities(self):
            """Get method for amenities"""
            from models import storage
            ap = []
            for val in storage.all(Amenity).values():
                if val.id in self.amenity_ids:
                    ap.append(val)
            return ap

        @amenities.setter
        def amenities(self, val=None):
            """Set method for amenities"""
            if type(val) is Amenity and val.id not in self.amenity_ids:
                self.amenity_ids.append(val.id)

        @property
        def reviews(self):
            """Get method for reviews"""
            from models import storage
            rp = []
            for val in storage.all(Review).values():
                if val.place_id == self.id:
                    rp.append(val)
            return rp
