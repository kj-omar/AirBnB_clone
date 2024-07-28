#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             nullable=False,
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             nullable=False,
                             primary_key=True)
                        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", back_populates="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                    back_populates="place_amenities",
                                    viewonly=False)      
    else:
        @property
        def reviews(self):
            """ review getter attribut for Filestorage """
            from models.engine.file_storage import FileStorage
            review_list = []
            for _, v in FileStorage.__objects.items():
                if v.place_id == self.id:
                    review_list.append(v)
                return review_list

        @property
        def amenities(self):
            """ amenities getter attribute for Filestorage """
            from models.engine.file_storage import FileStorage
            amenity_list = []
            for _, v in FileStorage.__objects.items():
                for id in self.amenity_ids:
                    if v.id == id:
                        amenity_list.append(v)
                return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """ amenities setter attribute """
            if type(obj) == "Amenity":
                self.amenity_ids.append(obj.id)
